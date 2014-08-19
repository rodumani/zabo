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
	applyEvent("#write");
});
