/**
 * Group
 * @namespace appGroup.group.services
 */
(function () {
    'use strict';

    angular
        .module('appGroup.group.services')
        .factory('Group', Group);

    Group.$inject = ['$http'];

    /**
     * @namespace Group
     * @returns {Factory}
     */
    function Group($http) {
        var Groups = {
            invite: invite,
            remove_member: remove_member,
            memberships: memberships,
            memberships_requests: memberships_requests,
            memberships_requests_confirm: memberships_requests_confirm
        };
        return Groups;

        function members(id){
            return $http.get('/api/v1/interest-groups/' + id + '/members/');
        }

        function memberships(){
            return $http.get('/api/v1/memberships/?group=' + String(group));
        }

        function memberships_requests(){
            return $http.get('/api/v1/memberships-requests/?group=' + String(group));
        }

        function memberships_requests_confirm(data){
            return $http.post('/api/v1/memberships-requests/'+ data.id +'/?group=' + String(group), data);
        }


        function invite(data){
            return $http.post('/api/v1/memberships-requests/?group=' + String(group), data);
        }

        function remove_member(id){
            return $http.delete('/api/v1/memberships/' + id + '/?group=' + String(group))
        }
    }

})();