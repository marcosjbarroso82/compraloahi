/**
 * Group
 * @namespace dashBoardApp.group.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.group.services')
        .factory('Group', Group);

    Group.$inject = ['$http'];

    /**
     * @namespace Group
     * @returns {Factory}
     */
    function Group($http) {
        var Groups = {
            create: create,
            detail: detail,
            destroy: destroy,
            update: update,
            list:list
        };

        return Groups;

        function list(){
            console.log('service list');
            return $http.get('/api/v1/interest-groups/');
        }

        function detail(id){
            return $http.get('/api/v1/interest-groups/' + id + '/');
        }

        function destroy(id){
            return $http.delete('/api/v1/interest-groups/' + id + '/');
        }

        function create(group){
            var fd = new FormData();
            fd.append('name', group.name);
            fd.append('description', group.description);
            fd.append('short_description', group.short_description);
            if (group.image != undefined) {
                fd.append('image', group.image);
            }
            return $http.post('/api/v1/interest-groups/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
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