var select_ids = [];
$(document).ready(function(e) {
	$('select#myselect option').each(function(index, element) {
		select_ids.push($(this).val());
	})
});

function selectAll()
{
	$('select#myselect').val(select_ids);
}

function deSelectAll()
{
	$('select#myselect').val('');
}