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
            list:list
        };

        return Post;

        function list(){
            return $http.get('/api/v1/posts/?group=' + String(group));
        }

        function create(post){
            return $http.post('/api/v1/posts/?group=' + String(group), post);
        }

    }

})();