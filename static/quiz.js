curr_answers = ["", "", "", "", ""]

/* Start of used by drag-drop only */
var display_answers = function(n, ans){
  $.each(ans, function(index,name){
    console.log("creating!")
    var char = String.fromCharCode(index+97);
    var id = "ans"+n+"_"+ char;
    var drag_answer = $("<div id='"+id+"' class='answer'><img "+name+"></div>").draggable({
      revert: "invalid",
      drag: function(event, ui) {
        $("#end"+n).addClass('blue');
      },
    });
    $("#start_drop"+"_"+n).append(drag_answer);
  })
}

// render feedback for drag-drop questions
var render_feedback_dd = function(n, feedback){
  for (var i = 0; i < 5; i++){
    j = i+1
    if (feedback[i] == 1){
      $("#end"+n+"_"+j).addClass("correct")
    }
    else {
      $("#end"+n+"_"+j).addClass("incorrect")
    }
  }
  if (n == 10) {
    $("#finish_btn").removeClass("hidden")
    $("#finish_btn").show()
  }
  else {
    $(".next_q_btn").show()
  }
}

// check if answers are dropped correctly
var check_answer_dd = function(n, qa){
  console.log("question: " + n)
  var data = {"question": n, "answer": qa}
  $.ajax({
    type: "POST",
    url: "/check_answer",
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify(data),
    success: function(result){
      var feedback = result["feedback"]
      var score = result["score"]
      render_feedback_dd(n, feedback)
    },
    error: function(request, status, error){
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
    }
  });
}

/* End of used by drag-drop only */

// render feedback for multiple choice and true/false
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
  $("#body_"+id+"_"+correct).addClass("green")
  if (ans != correct){
    $("#title_"+id+"_"+ans).addClass("red")
    $("#body_"+id+"_"+ans).addClass("red")
  }
  $(".pic_correct").removeClass("hidden")
  $(".pic_correct").show()

  $(".card").hover(function() {
    $(this).css("background-color", "transparent");},
  function() {
    $(this).css("background-color", "transparent");
  });
}

// check answer (communicate with server)
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

    display_answers(n, pics);
    $(".next_q_btn").hide()

    // droppable targets (start point)
    $(".start").droppable({
      over: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).addClass("highlight");
      },
      out: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).removeClass("highlight");
      },
    });

    // droppable targets (start point)
    $(".start").droppable({
      over: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).addClass("highlight");
      },
      out: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).removeClass("highlight");
      },
      drop: function (event, ui) {
        var draggableId = ui.draggable.attr("id");
        var draggableId_to_curr = draggableId.split('_')[1]
        curr_answers[draggableId_to_curr-97] = "";
      },
    });

    // droppable targets (end point)
    $(".end").droppable({
      over: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).addClass("highlight");
      },
      out: function( event, ui ){
        var id = $(this).attr("id");
        $("#"+id).removeClass("highlight");
      },
      drop: function (event, ui) {
        var draggableId = ui.draggable.attr("id");
        var draggableId_to_curr = draggableId.split('_')[1]
        var droppableId = parseInt($(this).attr("id").split('_')[1]);
        curr_answers[droppableId-1] = draggableId_to_curr;
        $(ui.draggable).offset($(this).offset());
      },
    });

    $("#submit_answer").click(function(){
      //var qa = $(this).attr("id").split("_") // question and answer in one list
      console.log("Current Answers: ", curr_answers)
      if ( (!(curr_answers.includes(""))) && ($(".next_q_btn").hasClass("hidden")) ) {
        check_answer_dd(n, curr_answers)
      }
    })

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
