$(document).ready(function(){
	$('.mini_video').click(function(event){
		$('.model').toggleClass('active');
		$('.wrapper').toggleClass('lock');
	});
});

$(document).ready(function(){
	$('.model').click(function(event){
		$('.model').removeClass('active');
		$('.wrapper').removeClass('lock');
	});
});
$(document).ready(function(){
	$('.model__close').click(function(event){
		$('.model').removeClass('active');
		$('.wrapper').removeClass('lock');
	});
});

$(document).ready(function(){
	$('.more__teachers').click(function(event){
		$('.teachers,.more,.less,.strelka__item').toggleClass('active');
	});
});
