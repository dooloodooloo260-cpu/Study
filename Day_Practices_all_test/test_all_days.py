import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from java_curriculum import LEVELS, LESSONS, render_lesson


ROOT = Path(__file__).resolve().parent.parent
DAY_COUNT = 90
PROBLEMS_PER_DAY = 5
DAY_FOLDER_PATTERN = re.compile(r"Day_Practices_(\d+)\Z")
PROBLEM_PATTERN = re.compile(
    r"(?P<position>\d+)\. "
    r"\[(?P<title>[^\]\r\n]+)\]"
    r"\((?P<url>https://leetcode\.com/problems/(?P<slug>[a-z0-9-]+)/)\)"
    r" — #(?P<number>\d+) · (?P<difficulty>Easy|Medium|Hard)\Z"
)
JAVA_EXAMPLES = {
    "TwoSum": "[0, 1]",
    "AddTwoNumbers": "7 -> 0 -> 8",
    "LongestSubstringWithoutRepeatingCharacters": "3",
    "MedianOfTwoSortedArrays": "2.0",
    "LongestPalindromicSubstring": "bab",
}


class AllDaysStructureTests(unittest.TestCase):
    def test_exactly_90_consecutive_day_folders_exist(self):
        expected = {f"Day_Practices_{day:02d}" for day in range(1, DAY_COUNT + 1)}
        actual = {
            path.name
            for path in ROOT.iterdir()
            if path.is_dir() and DAY_FOLDER_PATTERN.fullmatch(path.name)
        }

        self.assertEqual(
            expected,
            actual,
            f"Өдрийн хавтас дутуу эсвэл илүү байна. "
            f"Дутуу: {sorted(expected - actual)}; илүү/буруу: {sorted(actual - expected)}",
        )

    def test_every_day_has_five_valid_unique_problems(self):
        seen_numbers = {}
        seen_slugs = {}
        seen_titles = {}

        for day in range(1, DAY_COUNT + 1):
            with self.subTest(day=day):
                folder = ROOT / f"Day_Practices_{day:02d}"
                readme = folder / "README.md"
                self.assertTrue(readme.is_file(), f"{readme.relative_to(ROOT)} алга")
                text = readme.read_text(encoding="utf-8")
                lines = text.splitlines()

                self.assertTrue(
                    lines and lines[0] == f"# Day {day:02d}: LeetCode бодлого",
                    f"{readme.relative_to(ROOT)}: эхний мөрийн гарчиг буруу",
                )

                numbered_lines = [
                    (line_number, line)
                    for line_number, line in enumerate(lines, start=1)
                    if re.match(r"^\d+\.", line)
                ]
                self.assertEqual(
                    PROBLEMS_PER_DAY,
                    len(numbered_lines),
                    f"{readme.relative_to(ROOT)}: яг 5 дугаарласан бодлого байх ёстой",
                )

                day_numbers = []
                for expected_position, (line_number, line) in enumerate(
                    numbered_lines, start=1
                ):
                    match = PROBLEM_PATTERN.fullmatch(line)
                    self.assertIsNotNone(
                        match,
                        f"{readme.relative_to(ROOT)}:{line_number}: бодлогын мөрийн "
                        "формат буруу",
                    )
                    if match is None:
                        continue

                    problem = match.groupdict()
                    self.assertEqual(
                        str(expected_position),
                        problem["position"],
                        f"{readme.relative_to(ROOT)}:{line_number}: "
                        "бодлогын дараалал 1–5 байх ёстой",
                    )

                    number = int(problem["number"])
                    self.assertGreater(
                        number,
                        0,
                        f"{readme.relative_to(ROOT)}:{line_number}: "
                        "LeetCode дугаар эерэг байх ёстой",
                    )
                    day_numbers.append(number)

                    for seen, value, label in (
                        (seen_numbers, number, "дугаар"),
                        (seen_slugs, problem["slug"], "slug"),
                        (seen_titles, problem["title"].casefold(), "нэр"),
                    ):
                        self.assertNotIn(
                            value,
                            seen,
                            f"{readme.relative_to(ROOT)}:{line_number}: "
                            f"давхардсан бодлогын {label} ({value}); "
                            f"өмнө {seen.get(value, '')}",
                        )
                        seen[value] = readme.relative_to(ROOT)

                self.assertEqual(
                    PROBLEMS_PER_DAY,
                    len(set(day_numbers)),
                    f"{readme.relative_to(ROOT)}: нэг өдрийн бодлогууд давхардсан",
                )
                for label in ("Зорилго", "Хэрэглээ", "Бодох чиглэл"):
                    self.assertEqual(
                        PROBLEMS_PER_DAY,
                        sum(f"**{label}:**" in line for line in lines),
                        f"{readme.relative_to(ROOT)}: бүх бодлогод "
                        f"Монгол {label} байх ёстой",
                    )

    def test_java_curriculum_has_90_ordered_lessons_at_balanced_levels(self):
        self.assertEqual(DAY_COUNT, len(LESSONS), "Java хичээл яг 90 байх ёстой")
        self.assertEqual(
            [(1, 23, "Анхан шат"), (24, 46, "Дунд шат"),
             (47, 68, "Ахисан шат"), (69, 90, "Мэргэжлийн шат")],
            list(LEVELS),
            "Түвшний хуваарилалт 23/23/22/22 байх ёстой",
        )

        index = ROOT / "JAVA_CURRICULUM.md"
        self.assertTrue(index.is_file(), "JAVA_CURRICULUM.md алга")
        for day in range(1, DAY_COUNT + 1):
            with self.subTest(java_lesson_day=day):
                lesson = ROOT / f"Day_Practices_{day:02d}" / "JAVA_LESSON.md"
                self.assertTrue(lesson.is_file(), f"{lesson.relative_to(ROOT)} алга")
                self.assertEqual(
                    render_lesson(day),
                    lesson.read_text(encoding="utf-8"),
                    f"{lesson.relative_to(ROOT)} хөтөлбөрийн дараалалтай зөрсөн",
                )


class Day29JavaSolutionTests(unittest.TestCase):
    def test_all_java_sources_in_the_90_days_compile(self):
        source_files = sorted(
            str(path)
            for path in ROOT.glob("Day_Practices_[0-9][0-9]/**/*.java")
            if path.is_file()
        )
        self.assertTrue(source_files, "90 өдрийн хавтсанд Java source олдсонгүй")
        javac = shutil.which("javac")
        self.assertIsNotNone(javac, "Java JDK шаардлагатай: javac PATH-д олдсонгүй")

        with tempfile.TemporaryDirectory(prefix="all-day-java-tests-") as temp_dir:
            result = subprocess.run(
                [javac, "-encoding", "UTF-8", "-d", temp_dir, *source_files],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
            self.assertEqual(
                0,
                result.returncode,
                "90 өдрийн Java source компайл алдаа:\n"
                f"{result.stdout}{result.stderr}",
            )

    def test_five_java_solutions_compile_and_match_examples(self):
        day_folder = ROOT / "Day_Practices_29"
        expected_files = {f"{name}.java" for name in JAVA_EXAMPLES}
        actual_files = {path.name for path in day_folder.glob("*.java")}
        self.assertEqual(
            expected_files,
            actual_files,
            "Day 29-ийн Java шийдлийн файлууд дутуу эсвэл илүү байна",
        )

        javac = shutil.which("javac")
        java = shutil.which("java")
        self.assertIsNotNone(javac, "Java JDK шаардлагатай: javac PATH-д олдсонгүй")
        self.assertIsNotNone(java, "Java runtime шаардлагатай: java PATH-д олдсонгүй")

        with tempfile.TemporaryDirectory(prefix="day-practices-tests-") as temp_dir:
            output_dir = Path(temp_dir)
            source_files = [str(day_folder / filename) for filename in sorted(expected_files)]
            source_files.append(
                str(Path(__file__).resolve().parent / "Day29AlgorithmAssertions.java")
            )
            compile_result = subprocess.run(
                [javac, "-encoding", "UTF-8", "-d", str(output_dir), *source_files],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
            self.assertEqual(
                0,
                compile_result.returncode,
                "Day 29 Java компайл алдаа:\n"
                f"{compile_result.stdout}{compile_result.stderr}",
            )

            for class_name, expected_output in JAVA_EXAMPLES.items():
                with self.subTest(java_class=class_name):
                    result = subprocess.run(
                        [java, "-cp", str(output_dir), class_name],
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        timeout=15,
                        check=False,
                    )
                    self.assertEqual(
                        0,
                        result.returncode,
                        f"{class_name} ажиллуулахад алдаа:\n"
                        f"{result.stdout}{result.stderr}",
                    )
                    self.assertEqual(
                        expected_output,
                        result.stdout.strip(),
                        f"{class_name} жишээний хариу зөрсөн",
                    )

            edge_cases = subprocess.run(
                [java, "-cp", str(output_dir), "Day29AlgorithmAssertions"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
            self.assertEqual(
                0,
                edge_cases.returncode,
                "Day 29 edge-case шалгалт алдаа:\n"
                f"{edge_cases.stdout}{edge_cases.stderr}",
            )
            self.assertEqual(
                "Day 29 edge-case checks passed.",
                edge_cases.stdout.strip(),
                "Day 29 edge-case шалгалтын гаралт зөрсөн",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
