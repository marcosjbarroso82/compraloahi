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
            return $http.post('/api/v1/interest-groups/', group);
        }

        function update(group){
            return $http.put('/api/v1/interest-groups/' + group.id + '/', group);
        }

    }

})();