$(document).ready(function(){

  $(".card").click(function(){
    console.log("IEEIEIE")
    var card_id = ($(this).attr("id").split('_'))[1]
    window.location.href = "http://127.0.0.1:5000/flashcard/"+card_id+"";
  })
})
