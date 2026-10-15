CREATE SCHEMA IF NOT EXISTS quiz_app; 

CREAT TABLE IF NOT EXISTS quiz_app.questions (
    id SERIAL PRIMARY KEY, -- SERIAL = автомаар 1,2,3 ... нэмэгдэнэ
    question TEXT NOT NULL, -- NOT NULL = хоосон байж болохгүй 
    answer TEXT NOT NULL, 
    category VARCHAR(20) --'JAVA', 'english', 'behavioral'
);

-- === 2. 30 АСУУЛТ (6 insert) ===

INSERT INTO quiz_app.quistions (question, answer, category)
VALUES
('What does button mean? (1 = товч 2 = цонх)', '1', 'english'),
('How many buttons in CounterApp?', '2', 'java'),
('When to call setVisible?', '2', 'java'),
('What is JTextField(8)? (1 = тоо 2 = өргөн )', '2', 'java'),
('parseInt("5") = ?', '5', 'java'),
('frame.add(btn) does? (1 = remove 2 = add)', '2', 'java'),
('Without EXIT_ON_CLOSE? (1 = stop 2 = runs )', '2', 'java'),
('What is a label? (1 = шошго 2 = товч)', '1', 'english'),
('i % 2 == 0 means? (1=even 2=odd)', '1', 'java'),
('Even numbers 1-10?', '5', 'java'),
('count++ does? (1=decrease 2=increase)', '2', 'java'),
('i % 3 == ? for multiples of 3', '0', 'java'),
('Multiples of 3 in 1-30?', '10', 'java'),
('What is a window? (1=цонх 2=ширээ)', '1', 'english'),
('getText() does? (1=write 2=read)', '2', 'java'),
('setText() does? (1=show 2=delete)', '1', 'java'),
('CounterApp title?', 'Миний тоолуур', 'java'),
('Multiples of 5 in 1-20?', '4', 'java'),
('What does add mean? (1=нэмэх 2=хасах)', '1', 'english'),
('addActionListener does? (1=listens 2=draws)', '1', 'java'),
('Semicolon after if does? (1=correct 2=nothing)', '2', 'java'),
('Not divisible by 3 in 1-10?', '7', 'java'),
('What is result? (1=үр дүн 2=асуулт)', '1', 'english'),
('Where does int total = 0 go? (1=outside 2=inside)', '1', 'java'),
('Multiples of 10 in 1-100?', '10', 'java'),
('What is click? (1=repeat 2=press)', '2', 'english'),
('Result of "5" + 3? (1=8 2=53)', '2', 'java'),
('Divisible by 2 and 3 in 1-30?', '5', 'java'),
('Run command? (1=javac 2=java)', '2', 'java'),
('"I built a counter app" means? (1=хийсэн 2=хаасан)', '1', 'english');
-- == 3. шалгалт (5 select) ===
SELECT * FROM quiz_app.questions;
-- мөр
SElECT * FROM quiz_app.questions WHERE category = 'java'; 
-- шүүлт 

SELECT question, answer FROM quiz_app.questions LIMIT 5; ADD

-- эхний 5 

SELECT * FROM quiz_app.questions ORDER BY id DESC;

-- эсрэг дараалал 

SELECT COUNT(*) FROM quiz_app.questions;

хариу: 30 
