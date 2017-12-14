$(window).ready(function() {
	$.ajax({
		url:"https://acmp.ru/",
		success: function(result) {
			$("#root").html(result);
		}
	})
});
