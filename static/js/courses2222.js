$(document).ready(function(){
	// проверяем, какие чекбоксы активны и меняем сласс для родительского дива
    $('.direction__item').each(function(){
        var checkbox = $(this).find('input');
        if(checkbox.prop("checked")) $(this).addClass("active");
    });
    $('.courses_sort__item').each(function(){
        var checkbox = $(this).find('input');
        if(checkbox.prop("checked")) $(this).addClass("active");
    });

    // при клике по диву, делаем проверку
    $('.direction__item').click(function(){
    	$('.all input').prop('checked', false);
    	$('.all').removeClass("active");
        var checkbox = $(this).find('input');
        // если чекбокс был активен
        if(checkbox.prop("checked")){
            // снимаем класс с родительского дива
            $(this).removeClass("active");
            // и снимаем галочку с чекбокса
            checkbox.prop("checked", false);

        // если чекбокс не был активен
        }else{
            // добавляем класс родительскому диву
            $(this).addClass("active");
            // ставим галочку в чекбоксе
            checkbox.prop("checked", true);
        }

        var numberOfCheckboxesSelected = $('input:checkbox:checked').length;
        if(numberOfCheckboxesSelected == 0){
        	$('.all input').prop('checked', true);
    		$('.all').addClass("active");
        }
    });

    $('.all').click(function(){
    	$('.direction input').prop('checked', false);
    	$('.direction__item').removeClass("active");
    	$('.all input').prop('checked', true);
    	$('.all').addClass("active");

    });

    $('.item__type').click(function(){
    	var checkbox = $(this).find('input');
        // если чекбокс был активен
        if(checkbox.prop("checked")){
            checkbox.prop("checked", true);

        // если чекбокс не был активен
        }else{
            // добавляем класс родительскому диву
            $('.item__type').removeClass("active");
            $(this).addClass("active");
            // ставим галочку в чекбоксе
            checkbox.prop("checked", true);
        }
    });

    $('.item__hard').click(function(){
    	var checkbox = $(this).find('input');
        // если чекбокс был активен
        if(checkbox.prop("checked")){
            checkbox.prop("checked", true);

        // если чекбокс не был активен
        }else{
            // добавляем класс родительскому диву
            $('.item__hard').removeClass("active");
            $(this).addClass("active");
            // ставим галочку в чекбоксе
            checkbox.prop("checked", true);
        }
    });
});


$(document).ready(function(){
    $('.parametrs').click(function(event){
        $('.first,.second,.courses_sort').toggleClass('active');
    });
});
