$(document).ready(function(){
  $("#learn_positions_btn").click(function(){
    // learn positions page redirect
    window.location.href = "http://127.0.0.1:5000/learn";
  })

  $("#take_quiz_button").click(function(){
    window.location.href = "http://127.0.0.1:5000/quiz";
  })

  $("#start_learn_btn").click(function(){
    window.location.href = "http://127.0.0.1:5000/flashcard/1";
  })

  $("#checkpoint_feet").click(function(){
    window.location.href = "http://127.0.0.1:5000/review/1";
  })

  $("#checkpoint_quiz").click(function(){
    window.location.href = "http://127.0.0.1:5000/quiz";
  })

  $("#checkpoint_arms").click(function(){
    window.location.href = "http://127.0.0.1:5000/review/2";
  })

  $("#rev1_back").click(function(){
    window.location.href = "http://127.0.0.1:5000/flashcard/5";
  })
  $("#rev1_next").click(function(){
    window.location.href = "http://127.0.0.1:5000/flashcard/6";
  })
  $("#rev2_feet").click(function(){
    window.location.href = "http://127.0.0.1:5000/review/1";
  })
  $("#rev2_quiz").click(function(){
    window.location.href = "http://127.0.0.1:5000/quiz";
  })
  $("#begin_quiz_btn").click(function(){
    console.log("redirecting to quiz")
    window.location.href = "http://127.0.0.1:5000/quiz/1";
  })

  $("#final_review").click(function(){
    window.location.href = "http://127.0.0.1:5000/flashcard/1";
  })
  $("#final_quiz").click(function(){
    window.location.href = "http://127.0.0.1:5000/quiz";
  })
  $("#final_dance").click(function(){
    window.location.href = "http://127.0.0.1:5000/classes";
  })
})
