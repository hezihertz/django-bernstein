$('#sticky-nav').affix({
	offset: $('#sticky-nav').position()
});
$('body').scrollspy();
$(document).ready(function() {
	setTimeout(updateScrollSpy, 1000);
});
function updateScrollSpy() {
	$('body').each(function() {
		var $spy = $(this).scrollspy('refresh')
	});
};

$(document).foundation();
