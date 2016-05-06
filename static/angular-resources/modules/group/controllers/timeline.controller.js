/**
 * TimeLineCtrl
 * @namespace appGroup.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('appGroup.group.controllers')
        .controller('TimeLineCtrl', TimeLineCtrl);

    TimeLineCtrl.$inject = ['Post', '$sce', 'AlertNotification'];

    /**
     * @namespace TimeLineCtrl
     */
    function TimeLineCtrl(Post, $sce, AlertNotification){
        var vm = this;

        vm.post = {
            content: '',
            group: group
        };
        vm.posts = [];

        vm.submit = function(){
            Post.create(vm.post).then(successPost, errorPost);

            function successPost(data){
                AlertNotification.success("El post se creo con exito.")
                vm.posts.unshift(data.data);
            }

            function errorPost(data){
                AlertNotification.error("Error al intentar crear el post");
            }
        };

        init();
        function init(){
            Post.list().then(successGetPosts, errorGetPosts);

            function successGetPosts(data){
                vm.posts = data.data.results;
            }

            function errorGetPosts(data){
                AlertNotification.error("Error al intentar cargar los post, vuelva a intentarlo mas tarde.");
            }
        }


        vm.safeHtml = function(html){
            return $sce.trustAsHtml(html);
        };

    }
})();