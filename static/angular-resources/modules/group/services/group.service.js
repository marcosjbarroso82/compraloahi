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
            members: members,
            invite: invite,
            remove_member: remove_member,
            membership: membership
        };
        return Groups;

        function members(id){
            return $http.get('/api/v1/interest-groups/' + id + '/members/');
        }

        function membership(){
            console.log("SERVICE GET MEMBERSHIP");
            return $http.get('/api/v1/membership/?group=' + String(group));
        }

        function invite(id, data){
            return $http.post('/api/v1/interest-groups/' + id + '/invite/', data);
        }

        function remove_member(id, member){
            console.log("REMOVE MEMBER");
            console.log(member);
            return $http.delete('/api/v1/interest-groups/' + id + '/remove_member/?user=' + String(member.id), { 'user': member.id })
        }
    }

})();