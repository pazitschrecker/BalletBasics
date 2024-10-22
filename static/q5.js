curr_answers = ["", "", "", "", ""]

// display answers
var display_answers = function(n, ans){
  $.each(ans, function(index,name){
    console.log("creating!")
    var char = String.fromCharCode(index+97);
    var id = "ans"+n+"_"+ char;
    var drag_answer = $("<div id='"+id+"' class='answer col-md-2'><img "+name+"></div>").draggable({
      revert: "invalid",
      drag: function(event, ui) {
        $("#end"+n).addClass('blue');
      },
    });
    $("#start_drop"+"_"+n).append(drag_answer);
  })
}

var render_feedback_dd = function(n, feedback){
  console.log(feedback)
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

$(document).ready(function(){
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
      curr_answers[droppableId-1] = draggableId_to_curr
    },
  });

  $("#submit_answer").click(function(){
    //var qa = $(this).attr("id").split("_") // question and answer in one list
    console.log("Current Answers: ", curr_answers)
    if ( (!(curr_answers.includes(""))) && ($(".next_q_btn").hasClass("hidden")) ) {
      check_answer_dd(n, curr_answers)
    }
    //if ($("#fs"+q).hasClass("hidden")) {
      //check_answer5(qa)
    //}
  })

  // check answer (once all blocks placed)
})
