'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});

$(document).ready(function () {
	// humberger button
	$('#humberger-btn').click(function(){
		if ($(this).hasClass("opened")){
			$(this).removeClass("opened");
			$('#navbar').fadeOut(1000);
		}
		else{
			$(this).addClass("opened");
			$('#navbar').fadeIn(1000);
		}
	});
	$('.reply-btn').click(function(){
		$('#reply-to-input select').val($(this).attr('reply-to'));
	});
	//  main slider
	$("#slider").owlCarousel({
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
	$('.form-open').on('click', function () {
		$('#user-section , .background').fadeIn();
	});
	$('#form-close').on('click', function () {
		$('#user-section , .background').fadeOut();
	});

	// Back to top button
	
	$('.bck').backToTop({
		fxName : 'rightToLeft'
	});

	// sticky side bar in blogs and blog single
	$('#sidebar').stickySidebar({
		topSpacing: 50,
		bottomSpacing: 100,
	});
	

});
