$("#cubo, #consultas").hide();
$("#configuracion").submit(function(event){
	$("#cubo").show();
	event.preventDefault();
	$N = $("#configuracion #N").val();
	$("#qRestantes").text($("#configuracion #M").val());
	$("#configuracion #T").prop('disabled', true);
	$("input[id^='coor']").attr({"max":$N,"min":1});
	$("#coorv").attr({"max":"999","min":1});
	$("#formConfig").hide();
	$("#consultas").show();
	$("#configuracion #T").val($("#configuracion #T").val() - 1);
	
	$.post( "/", $(this).serialize(), function( data ) {
		$("input[id^='idCubo']").val(data["id"]);
	}, "json");
});
$("input[id^='coor']").change(function(){
	var nombre = $(this).attr("id").split("coor")[1];
	$("#consul" + nombre).text($(this).val());
});
$("input[name='optionsRadios']").click(function(){
	var nombre = $(this).attr("id");
	if (nombre == "radio1"){
		$("#update").show();
		$("#query").hide();
	}else{
		$("#update").hide();
		$("#query").show();
	}
});

function verModal(texto, respuesta){
	$("#myModal").modal("show");
	$("#parrafo").text(texto);
	$("#respuesta").text(respuesta);
}

$("form[id^='form_']").submit(function(){
	event.preventDefault();
	var nombre = $(this).attr("id").split("_")[1];
	$.post( "/" + nombre + "/", $(this).serialize(), function( data ) {
		verModal(data.con, data.respuesta);
		var numero = parseInt($("#qRestantes").text());
		if (numero != 1){
			$("#qRestantes").text(numero - 1);
		}else{
			$("#formConfig").show();
			$("#consultas").hide();
			if ($("#configuracion #T").val() == 0){
				$("#configuracion #T").prop('disabled', false);
				$('#configuracion').trigger('reset');
			}
		}
	}, "json");
	$(this).trigger('reset');
});