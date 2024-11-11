// Sample question data
const questions = [
    {
        question: "What is the capital of India?",
        options: ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        correctAnswer: "New Delhi"
    },
    // Add more questions here
];

let currentQuestion = 0;
let score = 0;
let userAnswers = [];

document.addEventListener('DOMContentLoaded', () => {
    loadQuestion();
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('prev-btn').addEventListener('click', prevQuestion);
    document.getElementById('submit-btn').addEventListener('click', submitTest);
});

function loadQuestion() {
    let q = questions[currentQuestion];
    document.getElementById('question').innerText = q.question;
    document.querySelectorAll('.options label').forEach((label, index) => {
        label.innerText = `${q.options[index]}`;
        label.previousElementSibling.value = q.options[index];
    });
}

function nextQuestion() {
    saveAnswer();
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        loadQuestion();
    }
}

function prevQuestion() {
    if (currentQuestion > 0) {
        currentQuestion--;
        loadQuestion();
    }
}

function saveAnswer() {
    let selectedOption = document.querySelector('input[name="option"]:checked');
    if (selectedOption) {
        userAnswers[currentQuestion] = selectedOption.value;
    }
}

function submitTest() {
    saveAnswer();
    // Calculate score
    score = userAnswers.reduce((acc, answer, index) => {
        return answer === questions[index].correctAnswer ? acc + 1 : acc;
    }, 0);
    alert(`You scored ${score} out of ${questions.length}`);
}
