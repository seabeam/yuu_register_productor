jQuery(document).ready(function($){
	var $sub_menu = $('.yuu-reg-block'),
		$dummy_anchor = $(".section");

	$sub_menu.children('a').on('click', function(event) {
		event.preventDefault();
		$(this).toggleClass('block-open').next('ul').slideToggle(200).end().parent('.yuu-reg-block').siblings('.yuu-reg-block').children('a').removeClass('block-open').next('ul').slideUp(200);
	});

	$dummy_anchor.addClass("yuu-dummy-anchor");
});
