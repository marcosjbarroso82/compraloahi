/**
 * Post
 * @namespace appGroup.group.services
 */
(function () {
    'use strict';

    angular
        .module('appGroup.group.services')
        .factory('Post', Post);

    Post.$inject = ['$http'];

    /**
     * @namespace Post
     * @returns {Factory}
     */
    function Post($http) {
        var Post = {
            create: create,
            detail: detail,
            destroy: destroy,
            update: update,
            list:list
        };

        return Post;

        function list(){
            return $http.get('/api/v1/post/');
        }

        function detail(id){
            return $http.get('/api/v1/interest-groups/' + id + '/');
        }

        function destroy(id){
            return $http.delete('/api/v1/interest-groups/' + id + '/');
        }

        function create(post){
            return $http.post('/api/v1/post/', post);
        }

        function update(group){
            var fd = new FormData();
            fd.append('name', group.name);
            fd.append('description', group.description);

            if (group.image && typeof group.image != 'string' && group.image != undefined) {
                fd.append('image', group.image);
            }
            return $http.patch('/api/v1/interest-groups/' + group.id + '/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

    }

})();