function render_feedback(id, feedback, correct, ans){
  $(".feedback_section").val("")
  $(".feedback_section").append(feedback);
  $(".feedback_section").removeClass("hidden")
  $(".feedback_section").show()
  if (id == "10") {
    $("#finish_btn").removeClass("hidden")
    $("#finish_btn").show()
  }
  else {
    $(".next_q_btn").removeClass("hidden")
    $(".next_q_btn").show()
    console.log("hey")
  }

  var c = "#title_"+id+"_"+correct
  $(c).addClass("green")
  if (ans != correct){
    $("#title_"+id+"_"+ans).addClass("red")
  }
  $(".pic_correct").removeClass("hidden")
  $(".pic_correct").show()
}

var check_answer = function(qa){
  var data = {"question": qa[0], "answer": qa[1]}
  console.log("REGULAR CHECKING")
  $.ajax({
    type: "POST",
    url: "/check_answer",
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify(data),
    success: function(result){
      var feedback = result["feedback"]
      var score = result["score"]
      var correct = result["correct"]
      render_feedback(qa[0], feedback, correct, qa[1])
    },
    error: function(request, status, error){
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
    }
  });
}

$(document).ready(function(){
    $(".next_q_btn").hide()
    $("#finish_btn").hide()

    $(".quiz_answer").click(function(){
    console.log("Clicked an answer")
    var qa = $(this).attr("id").split("_") // question and answer in one list
    var q = qa[0]
    if ($("#fs"+q).hasClass("hidden")) {
      check_answer(qa)
    }
    })


  $(".next_q_btn").click(function(){
    var id = parseInt($(this).attr("id").split("_").pop())
    var next_id = id+1
    window.location.href = "http://127.0.0.1:5000/quiz/"+next_id+"";
  })

  $("#finish_btn").click(function(){
    window.location.href = "http://127.0.0.1:5000/finish";
  })
})
