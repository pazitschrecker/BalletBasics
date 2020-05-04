$(document).ready(function(){
  if (id==1){
    $("#prev_1").addClass("disabled");
  }
  else{
    $("#prev_").removeClass("disabled");
  }

  $(".flip-card-front").click(function(){
    console.log("Hi")
    $(".flip-card-inner").css("transform", "rotateY(180deg)");
    $("#flip_").hide();
  });
  $(".flip-card-back").click(function(){
    console.log("Hi")
    $(".flip-card-inner").css("transform", "rotateY(0)");
    $("#flip_").hide();
  });

  $(".prev_btn").click(function(){
    var id = parseInt($(this).attr("id").split("_").pop())
    var prev_id = id-1;
    console.log(prev_id)
    if (id > 1){
      window.location.href = "http://127.0.0.1:5000/flashcard/"+prev_id+"";
    }
  })

  $(".next_btn").click(function(){
    var id = parseInt($(this).attr("id").split("_").pop())
    var next_id = id+1;
    console.log(next_id)
    if (id == 5) {
      window.location.href = "http://127.0.0.1:5000/review/1";
    }
    else if (id == 10) {
      window.location.href = "http://127.0.0.1:5000/review/2";
    }
    else {
      window.location.href = "http://127.0.0.1:5000/flashcard/"+next_id+"";
    }
  })

  $("#start_reviewbtn_10").click(function(){
    window.location.href = "http://127.0.0.1:5000/checkpoint";
  })
})
