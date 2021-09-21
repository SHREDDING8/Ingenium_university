$(document).ready(function(){
	$('.header__burger').click(function(event){
		$('.list__mob,.list__menu,.black__list,.burger_active,.burger_no_active,.content').toggleClass('active');
		$('.wrapper').toggleClass('lock');
	});
});


$(document).ready(function(){
	$('.course').click(function(event){
		$('.inside__list_item_course,.course').toggleClass('active');
	});
});

$(document).ready(function(){
	$('.about').click(function(event){
		$('.inside__list_item_about,.about').toggleClass('active');
	});
});

$(document).ready(function(){
	$('.webinars').click(function(event){
		$('.inside__list_item_webinars,.webinars').toggleClass('active');
	});
});