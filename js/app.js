$(window).ready(function() {
	$.ajax({
		url:"http://acmp.ru/",
		success: function(result) {
			$("#root").html(result);
		}
	})
});
