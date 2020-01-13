jQuery(document).ready(function($){
	var $lateral_menu_trigger = $('#yuu-menu-trigger'),
		$content_wrapper = $('.yuu-main-content'),
		$navigation = $('header'),
		$dummy_anchor = $(".section"),
		$menu_icon = $(".yuu-menu-icon");

	$lateral_menu_trigger.on('mouseenter', function() {
		$lateral_menu_trigger.css({"background":"#59716f"});
	});
	$lateral_menu_trigger.on('mouseleave', function() {
		$lateral_menu_trigger.css({"background":"#64807d"});
	});
	$lateral_menu_trigger.on('mousedown', function() {
		$lateral_menu_trigger.css({"background":"#4e6361"});
	});
	$lateral_menu_trigger.on('mouseup', function() {
		$lateral_menu_trigger.css({"background":"#64807d"});
	});

	$lateral_menu_trigger.on('click', function(event) {
		event.preventDefault();
		
		$lateral_menu_trigger.toggleClass('is-clicked');
		$navigation.toggleClass('address-map-open');
		$content_wrapper.toggleClass('address-map-open').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
			$('body').toggleClass('overflow-hidden');
		});
		$('.yuu-address-map').toggleClass('address-map-open');
		
		if($('html').hasClass('no-csstransitions')) {
			$('body').toggleClass('overflow-hidden');
		}
	});

	$content_wrapper.on('click', function(event) {
		if (!$(event.target).is('#yuu-menu-trigger, #yuu-menu-trigger span')) {
			$lateral_menu_trigger.removeClass('is-clicked');
			$navigation.removeClass('address-map-open');
			$content_wrapper.removeClass('address-map-open').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
				$('body').removeClass('overflow-hidden');
			});
			$('.yuu-address-map').removeClass('address-map-open');
			if($('html').hasClass('no-csstransitions')) {
				$('body').removeClass('overflow-hidden');
			}

		}
	});

	$('.yuu-reg-block').children('a').on('click', function(event) {
		event.preventDefault();
		$(this).toggleClass('block-open').next('ul').slideToggle(200).end().parent('.yuu-reg-block').siblings('.yuu-reg-block').children('a').removeClass('block-open').next('ul').slideUp(200);
	});

	$dummy_anchor.addClass("yuu-dummy-anchor");
});
