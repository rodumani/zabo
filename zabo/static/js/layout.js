function applyEvent(id) {
	$(id).mouseenter(function(){
		$(id).addClass("mouseover");
		$(id+">.subcategory").show();
	});
	$(id).mouseleave(function(){
		$(id).removeClass("mouseover");
		$(id+">.subcategory").hide();
	});
}

$(document).ready(function(){
	applyEvent("#category");
	applyEvent("#sitemap");
	$(".logio").mouseenter(function(){
		$("#account_action").show();
	});
	$(".logio").mouseleave(function(){
		$("#account_action").hide();
	});
});
