<template>
  <div class="quiz-container">
    <!-- Submit Button (Top Right) -->
    <button class="submit-button" @click="submitQuiz">Submit</button>

    <!-- Quiz Title (Editable) -->
    <div class="quiz-title">{{ quizTitle }}</div>

    <!-- Description, Deadline, and Points Section -->
    <div class="description-container">
      <!-- Non-editable description -->
      <div class="quiz-description">{{ quizDescription }}</div>

      <div class="deadline-and-points">
        <!-- Submission Deadline -->
        <p class="submission-deadline">Submissions will close Dec 8, 2024, 11:59 PM</p>

        <!-- Points Section -->
        <div class="quiz-points-section">
          <div class="quiz-points-box">{{ quizPoints }}</div>
          <span class="points-label">Points</span>
        </div>
      </div>
    </div>

    <hr class="divider" />
    <!-- Question Boxes -->
    <div v-for="(question, index) in questions" :key="index" class="question-box">
      <div class="orange-border"></div>

      <!-- Question Input (Non-editable) -->
      <div class="question-header">
        <div class="question-text">{{ question.text }}</div>
        <div class="question-type">
          <label>
            <input type="radio" v-model="question.type" value="multiple" disabled />
            <span>Multiple choice</span>
          </label>
        </div>
      </div>

      <!-- Options List (Non-editable) -->
      <div v-for="(option, optionIndex) in question.options" :key="optionIndex" class="option">
        <input type="radio" name="answer" :value="option" v-model="question.selectedAnswer" />
        <div class="option-text">{{ option }}</div>
      </div>

      <!-- Answer Key (Non-editable) -->
      <div class="answer-key">
        <span class="answer-label">✔ Answer key</span>
        <span>(</span>
        <div class="answer-points">{{ question.answerPoints }}</div>
        <span>points)</span>
      </div>
    </div>

  </div>
</template>

<script>
  import { ref } from "vue";

  export default {
    setup() {
      const quizTitle = ref("Quiz Title");
      const quizDescription = ref("Description");
      const quizPoints = ref(100);
      const questions = ref([
        {
          text: "question1",
          type: "multiple",
          options: ["option1", "option2", "option3"],
          selectedAnswer: null,
          answerPoints: 5,
        },
        {
          text: "What is 2 + 2?",
          type: "multiple",
          options: ["3", "4", "5"],
          selectedAnswer: null,
          answerPoints: 5,
        },
        {
          text: "question3'?",
          type: "multiple",
          options: ["option1", "option2", "option3"],
          selectedAnswer: null,
          answerPoints: 5,
        },
      ]);

      const submitQuiz = () => {
        console.log({
          quizTitle: quizTitle.value,
          quizDescription: quizDescription.value,
          quizPoints: quizPoints.value,
          questions: questions.value,
        });
        alert("Quiz Submitted!");
      };

      return {
        quizTitle,
        quizDescription,
        quizPoints,
        questions,
        submitQuiz,
      };
    },
  };
</script>
<style scoped>
  /* General container */
  .quiz-container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    position: relative;
  }

  /* Submit Button (Top Right) */
  .submit-button {
    position: absolute;
    top: 20px;
    right: 20px;
    padding: 8px 20px;
    background: #201887;
    color: white;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
    transition: 0.3s;
    border: none;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  }

    .submit-button:hover {
      background: darkorange;
    }

  .quiz-title {
    font-size: 24px;
    font-weight: bold;
    color: black; /* Ensure it's black */
    margin-bottom: 12px;
  }
  /* Disabled radio button */
  input[type="radio"]:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }

  /* Description & Deadline Container */
  .description-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .deadline-and-points {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  /* Smaller Description Box */
  .quiz-description {
    width: 60%;
    height: 50px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    resize: none;
  }

  /* Submission Deadline */
  .submission-deadline {
    font-size: 14px;
    color: black;
    margin-left: 15px;
    flex-shrink: 0;
  }

  /* Points Section */
  .quiz-points-section {
    display: flex;
    align-items: center;
    margin-top: 10px;
    justify-content: flex-end;
    gap: 10px;
  }

    .quiz-points-section label {
      font-size: 12px;
      font-weight: 500; /* Medium weight */
      margin-right: 10px;
    }

  .quiz-points-input {
    width: 80px;
    text-align: center;
    border: 1px solid #ddd;
    padding: 5px;
    border-radius: 4px;
  }

  /* Divider */
  .divider {
    margin: 20px 0;
    border: 0.5px solid #ddd;
  }

  /* Question Box */
  .question-box {
    position: relative;
    background: #f9f9f9;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid #ddd;
    margin-bottom: 20px;
  }

  .quiz-points-box {
    width: 60px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    font-weight: bold;
    text-align: center;
    padding: 5px;
  }


  /* Orange Side Border */
  .orange-border {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 5px;
    background: orange;
    border-radius: 6px 0 0 6px;
  }

  /* Question Input */
  .question-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .question-input {
    padding: 6px; /* Reduced padding */
    width: 60%; /* Set a fixed width percentage or adjust as needed */
    min-width: 200px; /* Optional: Set a minimum width */
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 12px;
  }

  /* Options */
  .option {
    display: flex;
    align-items: center;
    margin-top: 8px;
  }

  .option-input {
    width: 60%; /* Set a fixed width percentage (adjust as needed) */
    padding: 6px; /* Reduced padding for smaller height */
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 12px;
  }

  /* Add Option */
  .add-option {
    font-size: 14px;
    color: blue;
    margin-top: 10px;
    cursor: pointer;
    background: none;
    border: none;
    text-decoration: underline;
  }

  /* Answer Key */
  .answer-key {
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #555;
  }

  .answer-label {
    font-size: 12px;
    font-weight: 600; /* Slightly bolder for emphasis */
    margin-right: 6px;
  }

  .answer-points {
    width: 50px;
    text-align: center;
    border: 1px solid #ddd;
    padding: 5px;
    border-radius: 4px;
    margin: 0 5px;
  }

  /* General label styles */
  label {
    font-size: 12px;
    font-weight: 400; /* Normal weight */
    color: #333;
  }

  /* Specific label styles */
  .question-type label {
    font-size: 12px;
    font-weight: 500; /* Medium weight */
  }

  .answer-key span {
    font-size: 12px;
    font-weight: 400;
  }

  /* Media Query for smaller screens */
  /* Media Query for smaller screens */
  @media (max-width: 768px) {
    /* Adjusting the container to be more compact */
    .quiz-container {
      padding: 15px;
      max-width: 100%;
    }

    /* Adjusting the quiz title input */
    .quiz-title {
      font-size: 22px;
      margin-bottom: 10px;
    }

    /* Adjusting description box width */
    .quiz-description {
      width: 100%;
      height: 40px;
      padding: 8px;
      font-size: 13px;
    }

    /* Adjusting the submission deadline and points section */
    .deadline-and-points {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 5px;
    }

    .submission-deadline {
      font-size: 13px;
      margin-left: 0;
    }

    .quiz-points-section {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: 10px;
    }

    /* Adjust the question header input for smaller screens */
    .question-header {
      flex-direction: column;
      align-items: flex-start;
    }

    .question-text {
      font-size: 14px;
    }

    .question-type label {
      font-size: 13px;
    }

    /* Adjust the options input for smaller screens */
    .option-input {
      width: 100%;
      font-size: 12px;
    }

    /* Modify the points section for better fit */
    .quiz-points-section {
      align-items: flex-start;
      gap: 8px;
    }

    /* Adjust the add option button style */
    .add-option {
      font-size: 12px;
    }

    /* Answer key styling */
    .answer-key {
      font-size: 12px;
    }

    .answer-points {
      width: 45px;
      font-size: 12px;
    }

    .answer-label {
      font-size: 13px;
    }

    .submit-button {
      position: absolute;
      top: 15px;
      right: 15px;
      padding: 8px 16px;
      font-size: 14px;
    }

    /* Divider */
    .divider {
      margin: 15px 0;
      border: 0.5px solid #ddd;
    }
  }

</style>
