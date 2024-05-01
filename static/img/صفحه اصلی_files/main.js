'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});
//  main slider
$(document).ready(function(){
	$(".slider").owlCarousel({
		slideSpeed : 300,
		paginationSpeed: 300,
		items : 1, 
		itemsDesktop : false,
		itemsDesktopSmall : false,
		itemsTablet: false,
		itemsMobile: false ,
		loop:true,
		rtl: true,
		nav: true,
		navText: ['', '<span></span><span></span><span></span>'],
		animateOut: 'slideOutLeft',
		animateIn: 'slideInRight',
		autoplay:true,	
		autoplayTimeout: 10000,
		autoplayHoverPause:true
	});

	// more blogs slider
	$(".blogs-more").owlCarousel({
		items : 3,
		responsive:{
			0:{
				items:1,
				nav:true
			},
			720:{
				items:2,
			},
			1170:{
				items:3,
			}
		},
		loop: true,
		rtl: true,
		autoplay:true,	
		autoplayTimeout: 10000,
		autoplayHoverPause:true
	});
	// login / regsiter slider (pagination)
	var userSection = $("#user-section")
	userSection.owlCarousel({
		items : 1,
		rtl: true,
		mouseDrag: false,
		dotsData: true,
		slideSpeed : 500,
	});
	//  custome switcher for login / register slider
	$('#form-switcher input').on('click', function () {
		if ($(this).is(":checked")) {
			$('#register-btn').click()
		}
		else {
			$('#login-btn').click()
		}
		
	});
	$('#form-close').on('click', function () {
		$('#user-section , .background').fadeOut()
	});
	// Back to top button
	
	$('.bck').backToTop({
		fxName : 'rightToLeft'
	});

});
