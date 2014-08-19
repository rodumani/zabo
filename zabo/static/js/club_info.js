function edit_club_content() {
	var content = $("#club_content_edit").val();
	var club_name_en = $("#club_title").html();
	var url = window.location.pathname+"edit/";

	$.ajax({
		type : "GET",
		url : url,
		data : {
			club_name_en : club_name_en,
			content : content,
		},
		success : function(obj){
			$("#club_content").html(content);
			$(".club_edit").hide();
			$(".club_view").show();
		},
	});
}

$(document).ready(function(){
	$(".club_edit").hide();
	$("#club_content_edit").text($("#club_content").text());
	$("#edit_try").click(function(){
		$(".club_view").hide();
		$(".club_edit").show();
	});
	$("#edit_complete").click(function(){
		edit_club_content();
	});
});
