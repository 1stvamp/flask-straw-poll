(function($) {
    $(function() {
        $('table').chartify('pie');
        $('form').on('submit', function(e) {
            e.preventDefault();
            var el = $(e.target),
                data = el.serialize();
            
            $.post(el.attr('action'), data, function() {
                document.location.reload();
            });
        });
    });
})(jQuery);
