import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LEVELS = (
    (1, 23, "Анхан шат"),
    (24, 46, "Дунд шат"),
    (47, 68, "Ахисан шат"),
    (69, 90, "Мэргэжлийн шат"),
)

# Each entry is: lesson title, concept, coding exercise, completion criteria.
LESSONS = (
    ("Java орчин ба эхний програм", "JDK, JRE, JVM, source code-оос ажиллах програм болох үе шат.", "HelloWorld програм бичиж compile/run хийгээд гаралтыг өөрчил.", "Compile алдаагүй; эх код ба ажиллах үе шатыг тайлбарла."),
    ("Class ба main арга", "Class, main method, statement, block-ийн үүрэг.", "Өөрийн нэр, сурах зорилгоо хэвлэдэг `StudyProfile` class бич.", "Class нэр файлтайгаа таарч, нэг main method-оос эхэл."),
    ("Хувьсагч ба өгөгдлийн төрөл", "Primitive төрөл, String, зарлал ба анхны утга.", "Өдөр, нийт оноо, ахицын хувь хадгалж хэвлэ.", "Төрөл бүрээ зөв сонгож, утгын жишээ тайлбарла."),
    ("Оролт, гаралт ба оператор", "Scanner, арифметик болон харьцуулалтын оператор.", "Хоёр тоо авч нийлбэр, ялгавар, үржвэр, хуваалтыг хэвлэ.", "Тэгээр хуваахыг шалгаж, бүхэл ба бутархай хуваалтыг ялга."),
    ("Алгоритмыг алхмаар дүрслэх", "Оролт, гаралт, нөхцөл, давталттай псевдокод.", "Өдөр тутмын зорилго биелсэн эсэхийг шалгах алгоритм зур.", "Псевдокодыг Java мөр бүртэй нь холбож тайлбарла."),
    ("Операц тоолох ба Big O", "Өсөх n хэмжээтэй оролт дээр давталтын тоо хэрхэн өөрчлөгдөх.", "Нэг болон хоёр давхар давталтын алхмыг тооцож харьцуул.", "O(n), O(n²)-ыг жишээгээр тайлбарла."),
    ("Түгээмэл хугацааны төвөгшил", "O(1), O(log n), O(n), O(n log n), O(n²)-ын өсөлт.", "Өгөгдсөн таван псевдокодыг өсөлтийн ангилалд оруул.", "Өсөх дарааллыг зөв тогтоож, сонголтоо үндэслэ."),
    ("Нэмэлт санах ойн төвөгшил", "Оролтын хэмжээ болон нэмэлт санах ойн ялгаа; хэмжилтийн шударга нөхцөл.", "Массив хуулдаг болон in-place хувилбарын санах ойг харьцуул.", "Time/space complexity-г тусад нь бич."),
    ("Массив ба индекс", "Массивын тогтмол хэмжээ, индекс 0-оос эхлэх зарчим.", "5 өдрийн оноог массивт хадгалж, эхний ба сүүлийн элементийг хэвлэ.", "Хязгаараас гадуур индекс үүсгэхгүй бай."),
    ("Массивыг давтах", "For болон enhanced for ашиглан массив унших.", "Онооны массивын элемент бүрийг дугаартай нь хэвлэ.", "Хоёр давталтын аль тохирохыг сонгож тайлбарла."),
    ("Массивын нийлбэр ба дундаж", "Accumulator, тоолуур, хоосон оролтын нөхцөл.", "Оноонуудын нийлбэр болон дунджийг ол.", "Дунджийг бүхэл биш төрлөөр бодож, хоосон массивыг шалга."),
    ("Хамгийн их ба бага утга", "Нэг pass-д min/max олох инвариант.", "Массивын хамгийн их, хамгийн бага онооны индексийг ол.", "Нэг pass, O(n) хугацаанд зөв ажилла."),
    ("Массивт нэмэх ба хасах", "Шилжилт, хүчин чадал, индексийн шалгалт.", "Тогтмол массивт байрлалд утга оруулах, устгах аргыг бич.", "Эхлэл, төгсгөл, хоосон/дүүрэн нөхцөлийг шалга."),
    ("Хоёр хэмжээст массив", "Мөр, багана, nested loop болон матрицын индекс.", "Матрицын мөрийн нийлбэр болон диагональ нийлбэрийг ол.", "Мөр бүр ижил урттай гэж таамаглахгүйгээр хэмжээгээр давт."),
    ("String ба immutable утга", "String өөрчлөгддөггүй; дахин оноох ба шинэ объектын ялгаа.", "Өгүүлбэрийн урт, эхлэл, төгсгөлийг шалга.", "String-ийн аргыг зөв хэрэглэж, утгыг дахин оноохыг ойлго."),
    ("Тэмдэгт мөрийг унших", "charAt, индекс, Unicode code unit-ийн үндэс.", "Тэмдэгт мөрийн эгшиг, гийгүүлэгчийн тоог ол.", "Хоосон мөр ба зай/тэмдэгтийг алдаагүй тооц."),
    ("StringBuilder", "Олон дахин залгах үеийн хувиршгүй String-тэй зардлын ялгаа.", "Массивын үгсийг нэг мөр болгоод урвуугаар хэвлэ.", "Давталтын concatenate-ийн оронд StringBuilder хэрэглэ."),
    ("Тэмдэгт мөрийн энгийн шалгалтууд", "Тэмдэгтийн тоолол, palindrome ойлголт.", "Үг palindrome эсэхийг том/жижиг үсгийг нэгтгэн шалга.", "Хоосон, нэг тэмдэгт, зайтай оролтын дүрмээ тодорхойл."),
    ("Primitive ба reference", "Утгаар дамжуулах, объектын reference, aliasing.", "Primitive болон массивыг аргументад өгөөд өөрчлөлтийн ялгааг турш.", "Аль өөрчлөлт дуудсан талд харагдахыг тайлбарла."),
    ("Өөрийн class ба объект", "Field, constructor, method, `new`.", "Оноо хадгалж шинэчлэх `StudySession` class зохио.", "Объект бүр өөрийн тусдаа төлөвтэй бай."),
    ("Null ба хамгаалалт", "Null reference, null шалгалт, NullPointerException.", "Нэр эсвэл массив null байж болох method-уудыг аюулгүй болго.", "Null кейсийг тодорхой шалгаж, утгатай алдаа өг."),
    ("Объектын тэнцүү байдал", "Reference equality ба утгын equality; equals/hashCode ойлголт.", "Өөр ижил утгатай хоёр объектын == болон equals үр дүнг шалга.", "Identity ба logical equality-г андуурахгүй тайлбарла."),
    ("Encapsulation ба API", "Private field, validation, public method, invariant.", "Хувийн оноотой class бич; зөвшөөрөгдөхгүй утгыг хүлээн авахгүй болго.", "Төлөвийг шууд өөрчлөхгүй, class invariant-аа хадгал."),
    ("Хугацааны төвөгшил хэмжих", "Асимптотик үнэлгээ ба бодит benchmark-ийн хязгаар.", "Нэг массивыг O(n²) ба O(n log n) аргаар боловсруулж өсөлтийг харьцуул.", "Хэмжилтийн үр дүнгээр Big O-г баталж болохгүйг тайлбарла."),
    ("Массивын шугаман хайлт", "Нэг удаа шалгах, эхний тааралтын индекс, not-found төлөв.", "Target-ийн эхний индекс болон олдоогүй тохиолдлыг буцаа.", "Хоосон массив болон давхардсан утгыг турш."),
    ("Prefix sum", "Хэсэг нийлбэрийг prefix массив ашиглан O(1)-д авах.", "Олон range sum асуултад хариулах prefix sum class бич.", "Эхлэл/төгсгөлийн индексийн хязгаарыг шалга."),
    ("Two pointers ба sliding window", "Хоёр заагчийн инвариант; тасралтгүй цонхны төлөв.", "Эрэмбэлэгдсэн массиваас target нийлбэртэй хос олж, K урттай хамгийн их нийлбэрийг бод.", "Хоёр бодлогын хязгаарыг шалгаж, цаг/санах ойн төвөгшлийг тайлбарла."),
    ("Массивын хувиргалт ба давтамж", "In-place эргүүлэлт, modulo индекс, frequency Map.", "Массивыг k байрлал эргүүлж, элемент бүрийн давтамжийг тайлагна.", "k уртаас их, хоосон массив болон сөрөг утгыг зөв боловсруул."),
    ("String хайлт ба normalization", "String хоёр заагч, тэмдэгтийн давтамж, anagram, substring хайлт.", "Нормалчилсан palindrome, anagram, substring хайх гурван жижиг method бич.", "Том/жижиг үсэг, тэмдэгт, хоосон pattern-ийн дүрмийг тодорхойл."),
    ("Singly linked list: Node ба traversal", "Node-ийн утга, next reference, head/tail; head-аас null хүртэл алхах.", "Өөрийн Node class-аар жагсаалт үүсгэж хэвлээд, урт ба нийлбэрийг ол.", "Хоосон жагсаалт болон төгсгөлийн next null нөхцөлийг шалга."),
    ("Singly linked list: нэмэх", "Head/tail-д O(1)-ээр нэмэх.", "addFirst, addLast method-уудыг хэрэгжүүл.", "Хоосон жагсаалтад head ба tail хоёрыг зөв тохируул."),
    ("Singly linked list: устгах", "Өмнөх node-ийг хянах, head устгах онцгой тохиолдол.", "Утгаар нь эхний таарсан node-ийг устга.", "Толгой, сүүл, ганц node болон байхгүй утгыг турш."),
    ("Singly linked list: reverse", "Previous/current/next pointer шилжүүлэлт.", "Жагсаалтыг нэмэлт node үүсгэлгүй урвуул.", "Хоосон болон нэг node-той үед үр дүнг шалга."),
    ("Linked list: middle ба cycle", "Удаан/хурдан заагч; Floyd-ийн tortoise-hare алгоритм.", "Middle node болон cycle байгаа эсэхийг тус тус нэг pass-аар ол.", "Тэгш/сондгой урт, циклгүй, head болон дундаас эхлэх циклийг турш."),
    ("Linked list: dummy head", "Dummy/sentinel node-оор эхний node-ийн онцгой кейсийг арилгах.", "Тодорхой утгаас бага бүх node-ийг устгах method бич.", "Head дээр давхардсан хэд хэдэн node байхад зөв ажилла."),
    ("Doubly linked list: загвар", "prev/next холбоос болон head/tail invariant.", "Doubly linked list-ийн Node, жагсаалтын class зохио.", "Хоёр чиглэлд бүх холбоосоо баталгаажуул."),
    ("Doubly linked list: нэмэх", "Хоёр талаас head/tail-д холбоос шинэчлэх.", "addFirst болон addLast-г хэрэгжүүл.", "Хоосон болон нэг элементтэй үед холбоосоо шалга."),
    ("Doubly linked list: устгах", "Node-ийн өмнөх/дараах холбоосыг салгах.", "Node reference-аар O(1)-д устгах method бич.", "Толгой/сүүл устгахад head, tail зөв шинэчлэгд."),
    ("Stack: өөрийн хэрэгжүүлэлт", "Array-д суурилсан stack, capacity ба resize.", "Generic бус int stack-д push/pop/peek бич.", "Дүүрэлт болон хоосон үед explicit алдаа мэдээл."),
    ("Stack: LIFO ба Min Stack", "Push/pop/peek, underflow болон үе бүрийн minimum утгыг хянах.", "ArrayDeque-аар хаалт шалгаж, O(1) min-тэй MinStack хэрэгжүүл.", "Хаалтын алдаа, давхардсан minimum, хоосон pop-ийг шалга."),
    ("Stack: expression шалгах", "Stack ашиглан operator/operand-ийн дараалал боловсруулах.", "Reverse Polish notation илэрхийллийг бод.", "Хуваахын дараалал болон буруу илэрхийллийг шалга."),
    ("Queue: FIFO", "Offer/poll/peek ба null/хоосон нөхцөл.", "ArrayDeque ашиглан үйлчлүүлэгчийн дарааллыг загварчил.", "Оруулах дарааллаар гарч буйг баталгаажуул."),
    ("Queue: circular array", "Head/tail modulo, size, wrap-around.", "Fixed-capacity circular queue хэрэгжүүл.", "Олон enqueue/dequeue хийж wrap-around-ийг шалга."),
    ("Queue: BFS-ийн суурь", "Queue ашиглан түвшин тус бүрээр боловсруулах; хоёр stack-аар FIFO үүсгэх.", "Хоёр stack-тэй queue хэрэгжүүлээд grid-д хамгийн ойрын зорилгыг BFS-аар ол.", "FIFO дараалал хадгалж, нэг нүдийг хоёр дахин оруулахгүй тэмдэглэ."),
    ("Hash table: key ба value", "HashMap-ийн put/get/remove/containsKey.", "ID-аар суралцагч хайх Map үүсгэж CRUD үйлдэл хий.", "Байхгүй key ба давтан key-ийн дүрмийг тайлбарла."),
    ("Hash table: давтамж тоолох", "Map.merge/getOrDefault ашиглах.", "Массивын элементүүдийг давтамжаар нь тоолж хамгийн ихийг ол.", "Сөрөг утга болон тэнцүү давтамжийг тодорхой дүрмээр шийд."),
    ("Hashing ба collision", "hashCode, bucket, collision, load factor ойлголт.", "Collision гарах өөрийн key жишээг бодож, HashMap-д equals/hashCode хэрэгжүүл.", "equals тэнцүү бол hashCode адил байх дүрмийг мөрд."),
    ("Hash table: бүлэглэх", "Map утга болгон жагсаалт хадгалж бүлэг үүсгэх.", "Ижил анхны үсэгтэй үгсийг Map ашиглан бүлэглэ.", "Оролтын дарааллын шаардлага байгаа эсэхийг шийд."),
    ("Hash table: LRU загвар", "HashMap ба doubly linked list-ийн O(1) хамтын ажиллагаа.", "Хязгаартай LRU cache-ийн get/put бүтэц зохио.", "Capacity, cache hit, least-recently-used устгалын invariant-ыг тайлбарла."),
    ("Set ба давхардал арилгах", "HashSet-ийн unique membership болон add үр дүн.", "Массивын давхардлыг арилгаж unique утгууд гарга.", "Оролтын дараалал хадгалах шаардлагатай бол өөр collection сонго."),
    ("Set: олонлогийн үйлдэл", "Union, intersection, difference.", "Хоёр бүлгийн нийтлэг болон зөвхөн нэгэнд байгаа ID-г ол.", "Гаралтын олонлогийг жишээгээр шалга."),
    ("Set: эрэмбэлэгдсэн unique", "TreeSet-ийн эрэмбэ ба O(log n) үйлдлүүд.", "Давхардлыг арилгасан оноог эрэмбээр хэвлэ.", "HashSet ба TreeSet-ийн trade-off-ийг хэл."),
    ("Recursion: base ба шагнал", "Base case, recursive case, ахицын хэмжүүр.", "n-ээс 1 хүртэл буурах тоонуудыг рекурсээр хэвлэ.", "Base case хүрч, рекурсын дуудлагын дарааллыг тайлбарла."),
    ("Recursion: массив ба factorial", "Индексээр асуудлыг жижиглэх, үржвэрийн хуримтлал, overflow.", "Массивын нийлбэр болон factorial-ийг рекурсээр бод.", "Хоосон массив, сөрөг оролт, 0 ба integer хязгаарыг шалга."),
    ("Recursion: binary search", "Дэд мужид рекурсив хуваалт хийх.", "Binary search-ийн рекурсив хувилбар бич.", "Хязгаарын шинэчлэлтээр давталт/stack overflow үүсгэхгүй бай."),
    ("Memoization ба call tree", "Давхардсан дэд бодлого, exponential branching, cache.", "Fibonacci-ийн naive болон memoized хувилбарыг дуудлагын тоогоор харьцуул.", "Naive хувилбарын өсөлтийг тайлбарлаж, memoized O(n)-ийг батал."),
    ("Backtracking: subset", "Сонгох/алгасах салаалал, буцааж төлөв сэргээх.", "Бүх subset-ийг backtracking-аар үүсгэ.", "Оролтын n элементээс 2^n subset гарсныг шалга."),
    ("Insertion sort: үндсэн хувилбар", "Эрэмбэлэгдсэн prefix дотор элементийг оруулах.", "Insertion sort-ыг массив дээр in-place бич.", "Хоосон, урвуу, давхардсан массивыг эрэмбэл."),
    ("Insertion sort: тогтвортой байдал", "Тэнцүү key-тэй элементүүдийн анхны дарааллыг хадгалах.", "Оноо ба нэртэй объектуудыг оноогоор insertion sort хий.", "Тэнцүү оноотой хүний дараалал өөрчлөгдөхгүй бай."),
    ("Insertion sort: бараг эрэмбэлэгдсэн өгөгдөл", "Шилжилтийн тоо ба adaptive шинж.", "Эрэмбэлсэн ба бараг эрэмбэлсэн массивт shift тоолж харьцуул.", "Best O(n), worst O(n²)-ыг ажиглалтаар тайлбарла."),
    ("Insertion sort: boundary шалгалт", "Index decrement, key insertion, жижиг тестүүд.", "Сөрөг болон давхардсан утгатай массивыг эрэмбэлж assertion бич.", "Эрэмбэлэгдсэн эсэхийг тусдаа checker-ээр батал."),
    ("Merge sort: merge алхам", "Хоёр эрэмбэлэгдсэн хэсгийг нэг шугаман merge хийх.", "Хоёр эрэмбэлэгдсэн массивыг нэмэлт массивт нэгтгэ.", "Тэнцүү утгын тогтвортой дарааллыг хадгал."),
    ("Merge sort: рекурсив хуваалт", "Divide-and-conquer, midpoint, base case.", "Merge sort-ыг рекурсээр бүхэл массивт хэрэгжүүл.", "Оролтын массивын уртыг хадгалж, эрэмбэлэгдсэнийг шалга."),
    ("Merge sort: санах ой", "O(n) auxiliary space ба allocation удирдлага.", "Нэг туслах массивыг рекурсийн турш дахин ашигладаг хувилбар бич.", "Цаг O(n log n), санах ой O(n) гэж тайлбарла."),
    ("Merge sort: inversion тоолох", "Merge явцдаа урвуу хосуудыг тоолох.", "Массив хэдэн inversion-тэйг merge sort-той хамт тоол.", "Эрэмбэлсэн input 0, буурах input n(n-1)/2 байх."),
    ("Merge sort: linked list", "Linked list-ийг массив болголгүй хувааж merge хийх.", "Singly linked list-д merge sort хэрэгжүүл.", "Нэмэлт node-оор дүүргэхгүй, O(n log n) байлга."),
    ("Quick sort: partition", "Pivot-ийн хоёр талын partition invariant.", "Lomuto partition-ийг тусад нь бичиж үр дүнг шалга.", "Pivot-ийн өмнө бага/тэнцүү, дараа их утгууд байрлах."),
    ("Quick sort: рекурсив хувилбар", "Partition-ийн дараа хоёр талд рекурс хийх.", "In-place quicksort хэрэгжүүл.", "Давхардсан болон сөрөг утгатай оролтыг турш."),
    ("Quick sort: pivot ба worst case", "Pivot сонголт, sorted input, stack depth.", "Эхний/сүүлийн pivot-ийг random эсвэл median-of-three-тэй харьцуул.", "Worst-case O(n²) эрсдэлийг хэмжилт/тайлбараар харуул."),
    ("Quick sort: 3-way partition", "Dutch National Flag; давхардсан pivot-уудыг нэг pass-д ялгах.", "Олон давхардсан утгатай массивт 3-way quicksort хий.", "All-equal оролт дээр рекурсийн ажил эрс багасахыг шалга."),
    ("Binary search: lower bound", "Target-аас багагүй эхний индексийг олох.", "Давхардсан эрэмбэлэгдсэн массивт lowerBound бич.", "Target байхгүй, эхлэл/төгсгөлд байгааг турш."),
    ("Binary search: upper bound ба range", "Target-аас их эхний индекс, давхардлын хүрээ.", "Target-ийн эхний ба сүүлийн индексийг хоёр bound-оор ол.", "Хайлт тус бүр O(log n) байлга."),
    ("Binary search: эргүүлсэн массив", "Pivot-той эрэмбэлэгдсэн массивын хагас хэсгийг тодорхойлох.", "Unique элементтэй rotated array-д target хай.", "Хоосон, нэг элемент, эргэлтгүй кейсийг турш."),
    ("Binary search on answer", "Монотон боломжтой эсэх шалгалтаар хариуг хоёртын хайх.", "Ажлын хэмжээг k машинд хуваах хамгийн бага хугацааг ол.", "Feasibility predicate монотон гэдгийг нотол."),
    ("Tree: Node ба traversal", "Root, child, leaf, height; preorder/inorder/postorder.", "Binary tree үүсгэж гурван DFS traversal хэвлэ.", "Null node болон ганц root кейсийг турш."),
    ("Tree: түвшний traversal", "Queue ашиглан level-order traversal хийх.", "Binary tree-г түвшин тус бүрийн жагсаалтаар буцаа.", "Хоосон tree болон өргөн tree-г шалга."),
    ("Tree: height ба balance", "Өндөр, subtree мэдээллийг нэг pass-аар буцаах.", "Tree balanced эсэхийг O(n)-д шалга.", "Дэд модны өндрийг давтан тооцох O(n²) шийдлээс зайлсхий."),
    ("Tree: нийтлэг ancestor", "Recursive search ба LCA-ийн нөхцөл.", "Binary tree-ийн хоёр node-ийн lowest common ancestor-ийг ол.", "Node байхгүй/ижил node нөхцөлийг тодорхойл."),
    ("Binary Search Tree: invariant", "Зүүн тал бага, баруун тал их; duplicate дүрэм.", "BST-д утга хайх болон valid эсэхийг шалгах method бич.", "Зөвхөн эцэгтэй харьцуулахгүй, бүх ancestor-ийн хязгаарыг дамжуул."),
    ("BST: insert ба search", "Давталттай O(h) insert/search.", "BST-д олон утга оруулж, хайлтыг хэрэгжүүл.", "Duplicate бодлогыг ил тод сонго; skewed tree-ийн h-г тооц."),
    ("BST: remove", "Leaf, нэг child, хоёр child устгалын гурван тохиолдол.", "BST-ээс key устгах method бич.", "Устгасны дараа inorder нь эрэмбэлэгдсэн байх."),
    ("BST: range ба successor", "Inorder дараагийн утга, мужид хайх pruning.", "Өгөгдсөн мужийн утгууд болон successor-ийг ол.", "Шаардлагагүй subtree рүү орохгүй complexity-г тайлбарла."),
    ("Balanced tree: AVL ойлголт", "Balance factor, rotation хэрэгтэй болох нөхцөл.", "LL/RR insertion жишээг зурж аль rotation орохыг тодорхойл.", "Rotation дараа BST дараалал хадгалагдахыг шалга."),
    ("AVL: rotation хэрэгжүүлэх", "Left/right rotation болон өндөр шинэчлэх дараалал.", "AVL node-д height, balance factor тооцоод rotation хий.", "LL ба RR кейсийг автоматаар шалга."),
    ("Heap ба PriorityQueue", "Complete binary tree, parent/child индекс, heap order.", "Массивт min-heap insert ба sift-up хэрэгжүүл.", "Parent <= child invariant бүх индексэд хадгалагд."),
    ("Heap sort ба top-K", "Heapify, extract, PriorityQueue-ийн O(log n) үйлдэл.", "Их хэмжээний жагсаалтаас хамгийн их K утгыг heap-аар ол.", "Бүх массивыг эрэмбэлэхээс илүү тохирох heap хэмжээ сонго."),
    ("Graph: загвар ба BFS/DFS", "Adjacency list, directed/undirected, visited төлөв.", "Графын connected component-уудыг BFS/DFS-аар тоол.", "Disconnected graph-ийн бүх component-ийг эхлүүлж шалга."),
    ("Graph: cycle ба topological order", "Directed cycle болон dependency DAG-ийн дараалал.", "Course prerequisite-ийг adjacency list, indegree ашиглан эрэмбэл.", "Cycle илэрвэл боломжгүйг зөв мэдээл."),
    ("Shortest path: Dijkstra", "Non-negative edge, priority queue, stale entry.", "Жинтэй графын нэг эх үүсвэрээс хамгийн богино зай ол.", "Сөрөг жин орвол татгалз; unreachable node-г тусад нь илэрхийл."),
    ("Мэргэжлийн capstone: DSA сонголт", "Problem constraints-оос structure, algorithm, complexity сонгох.", "Өдөр тутмын суралцах tracker-д hash lookup, priority queue, graph dependency-г холбосон Java консоль төсөл зохио.", "Design note, edge-case тест, time/space complexity, цэвэр compile бүгдийг хүргэ."),
)


def level_for_day(day):
    for start, end, name in LEVELS:
        if start <= day <= end:
            return name
    raise ValueError(f"Өдрийн дугаар буруу: {day}")


def render_lesson(day):
    title, concept, exercise, completion = LESSONS[day - 1]
    level = level_for_day(day)
    return (
        f"# Day {day:02d}: {title}\n\n"
        f"**Түвшин:** {level}  \n"
        f"**Хичээлийн сэдэв:** {title}\n\n"
        f"## Суралцах зүйл\n\n{concept}\n\n"
        f"## Java дасгал\n\n{exercise}\n\n"
        f"## Дууссан гэж үзэх шалгуур\n\n{completion}\n\n"
        f"LeetCode-ийн тухайн өдрийн жагсаалт өөрчлөгдөөгүй; "
        f"[README.md](./README.md)-ээс үзнэ үү.\n"
    )


def render_index():
    lines = [
        "# Java Data Structures & Algorithms: 90 өдрийн хөтөлбөр",
        "",
        "Өдөр бүр нэг шаталсан Java хичээл, нэг хэрэгжүүлэлтийн дасгал хийнэ. "
        "LeetCode-ийн 90 өдрийн, өдөр бүр 5 бодлоготой жагсаалт тусдаа хэвээр.",
        "",
        "| Түвшин | Өдрүүд | Хичээлийн тоо | Гол зорилго |",
        "| --- | --- | ---: | --- |",
        "| Анхан шат | 01–23 | 23 | Java суурь, алгоритмын сэтгэлгээ, массив, мөр, reference |",
        "| Дунд шат | 24–46 | 23 | Массив/мөрийн арга, linked list, doubly linked list |",
        "| Ахисан шат | 47–68 | 22 | Stack, queue, hash table, set, recursion, sorting |",
        "| Мэргэжлийн шат | 69–90 | 22 | Sorting-ийн ахисан арга, binary search, tree/BST, AVL, heap, graph |",
        "",
        "Сэдвүүд зурагт харагдсан дарааллаар үргэлжилнэ. Зурагт түгжээтэй "
        "харагдсан BST-ээс цааш AVL, heap, graph зэрэг мэргэжлийн нэмэлт "
        "сэдвийг шаталсан байдлаар оруулав.",
        "",
        "## Хөтөлбөр",
    ]
    for start, end, level in LEVELS:
        lines.extend(("", f"### {level} — Day {start:02d}–{end:02d}", ""))
        for day in range(start, end + 1):
            title = LESSONS[day - 1][0]
            lines.append(
                f"- [Day {day:02d}: {title}](./Day_Practices_{day:02d}/JAVA_LESSON.md)"
            )
    lines.extend(
        (
            "",
            "## Одоогийн Java дасгалуудын шалгалтын тэмдэглэл",
            "",
            "- Одоогийн эхний өдрүүдэд Hello World, арифметик, нөхцөл, давталт, "
            "массив, тоолуурын дадлага байна; шинэ дараалалд эдгээрийг сууринаас "
            "нь дахин байршууллаа.",
            "- `Day_Practices_01/Java/Day01Text.java` нь Two Sum/HashMap шийдэл "
            "агуулдаг тул beginner-ийн анхны дасгал гэхээсээ ахисан жишээ. "
            "Хуучин файлыг хөдөлгөөгүй, шинэ хөтөлбөрт зөв түвшний дарааллаар оруулав.",
            "- `Day_Practices_02/Day02Text.java` бүхэл тооны хуваалтын үр дүн "
            "болон floating-point ялгааг харуулахад ашиглагдана.",
            "- `Day_Practices_19/LoopApp.java` давталтын `i` хувьсагч зарлаагүй "
            "байсан; compile алдааг засаж, 1–24 өдрийг хэвлэдэг болгосон.",
            "- `Day_Practices_26/CounterA03.java` анх дутуу байсан; 1–50 хүртэлх "
            "5-д хуваагдах тоог тоолдог ажиллах дасгал болгон дуусгав.",
            "- LeetCode жагсаалт болон Day 29-ийн таван Java шийдэлд хүрээгүй.",
            "",
            "## Бүх Java файлыг шалгах",
            "",
            "```sh",
            "build_dir=$(mktemp -d)",
            "find Day_Practices_[0-9][0-9] -type f -name '*.java' -print0 | xargs -0 javac -encoding UTF-8 -d \"$build_dir\"",
            "result=$?",
            "rm -rf \"$build_dir\"",
            "exit \"$result\"",
            "```",
            "",
        )
    )
    return "\n".join(lines)


def write_curriculum(root=ROOT):
    for day in range(1, 91):
        lesson_path = root / f"Day_Practices_{day:02d}" / "JAVA_LESSON.md"
        if not lesson_path.parent.is_dir():
            raise FileNotFoundError(f"Өдрийн хавтас алга: {lesson_path.parent}")
        lesson_path.write_text(render_lesson(day), encoding="utf-8")
    (root / "JAVA_CURRICULUM.md").write_text(render_index(), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build the 90-day Java curriculum files.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the curriculum index and 90 daily Java lesson files.",
    )
    args = parser.parse_args()
    if not args.write:
        parser.error("Файлууд үүсгэхийн тулд --write сонголтыг өгнө үү.")
    write_curriculum()
    print("JAVA_CURRICULUM.md болон 90 өдрийн JAVA_LESSON.md файл үүсгэлээ.")


if __name__ == "__main__":
    main()
