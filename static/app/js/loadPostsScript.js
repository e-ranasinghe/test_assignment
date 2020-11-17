(function ($) {
    $('#nextPosts').on('click', function () {
        var link = $(this);
        var page = link.data('page');

        $.ajax({
            type: 'post',
            url: '/next_posts/',
            data: {
                'page': page,
                'csrfmiddlewaretoken': window.CSRF_TOKEN
            },
            success: function (data) {
                if (data.has_next) {
                    link.data('page', page + 1);
                } else {
                    link.hide();
                }
                // append html to the posts div
                $('#posts').append(data.posts_html);
            },
            error: function (xhr, status, error) {
            }
        });
    });
}(jQuery));