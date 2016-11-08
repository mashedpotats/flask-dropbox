/**
 * Created by Samuel on 11/7/2016
 */
$(function () {
    var $tree = $('#tree');
    $tree.jstree({
        'core': {
            'data': [
                'Simple root node',
                {
                    'text': 'Root node 2',
                    'children': [
                        {'text': 'Child 1'},
                        'Child 2'
                    ]
                }
            ]
        }
    });

    $tree.on("changed.jstree", function (e, data) {
        console.log(data.selected);
    });
});