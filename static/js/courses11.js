$(document).ready(function(){
	$('.recommed').slick({
		autoplay:true,
		autoplaySpeed: 5000,
	});
});
$(document).ready(function(){
  $('.recommed').hover(
    function(e) {
      $('.slick-next,.slick-prev').toggleClass('active__hover')
    }
  );
});
