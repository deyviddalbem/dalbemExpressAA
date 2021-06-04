$(document).ready(function () {
    $('#tabelaUsuarios').DataTable({
    })
    
}).extend($.fn.dataTable.defaults, {
    dom: 'B<"clear">lfrtip',
    buttons: [
        { extend: 'csv', text: 'salvar em csv' },
        { extend: 'pdf', text: 'salvar em PDF' },
        { extend: 'print', text: 'imprimir' }
    ],
    searching: true,
    paging: true,
    autoWidth: true,
    responsive: true,
    columnDefs:[{
        className:'order-column',
    }],
    language: {
        "search": "Buscar na tabela:",
        "emptyTable": "Não existe dados a serem exibidos",
        "info": "Exibindo página _PAGE_ de: _PAGES_ páginas.",
        "zeroRecords": "Nenhum registro correspondente a pesquisa foi encontrado!",
        "loadingRecords": "Carregando...",
        "processing": "Processsando...",
        "paginate": {
            "first": "Primeira",
            "last": "Ultima",
            "next": "Próxima",
            "previous": "Anterior",
        },
        "lengthMenu": 'Filtrar <select>' +
            '<option value="1">01</option>' +
            '<option value="5">05</option>' +
            '<option value="10">10</option>' +
            '<option value="20">20</option>' +
            '<option value="50">50</option>' +
            '<option value="100">100</option>' +
            '<option value="-1">Todos</option>',
    }


});