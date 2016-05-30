/**
 * TimeLineCtrl
 * @namespace appGroup.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('appGroup.group.controllers')
        .controller('TimeLineCtrl', TimeLineCtrl);

    TimeLineCtrl.$inject = ['Post', '$sce', 'AlertNotification', 'Group'];

    /**
     * @namespace TimeLineCtrl
     */
    function TimeLineCtrl(Post, $sce, AlertNotification, Group){
        var vm = this;

        vm.post = {
            content: '',
            group: group
        };
        vm.posts = [];
        vm.group = {
            members: []
        };

        vm.memberships = [];
        vm.memberships_requests = [];
        vm.member_email = "";

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
            Post.list(group).then(successGetPosts, errorGetPosts);

            function successGetPosts(data){
                vm.posts = data.data.results;
            }

            function errorGetPosts(data){
                AlertNotification.error("Error al intentar cargar los post, vuelva a intentarlo mas tarde.");
            }

            if(has_permission){
                Group.memberships_requests().then(membershipsRequestsSuccess, membershipsRequestsError);
            }
            function membershipsRequestsSuccess(data){
                vm.memberships_requests = data.data.results;
            }

            function membershipsRequestsError(data){
                AlertNotification.error("Error");
            }

        }

        vm.inviteMember = function(){
            if(has_permission){
                Group.invite({ 'email':vm.member_email }).then(InviteMemberSuccess, InviteMemberError);
            }
            function InviteMemberSuccess(){
                AlertNotification.info("La invitacion fue exitosa, solo falta que la confirmacion de la otra persona.");
                vm.member_email = '';
            }

            function InviteMemberError(){
                AlertNotification.error("Error al tratar de crear la invitacion, chequee el email y vuelva a intentarlo.");
            }
        };

        var flag_get_user = false;
        vm.toggleUser = function(){

            if (!flag_get_user && has_permission){
                flag_get_user = true;

                Group.memberships().then(getGroupMembersSuccess, getGroupMembersError)
            }

            function getGroupMembersSuccess(data){
                vm.memberships = data.data.results;
            }

            function getGroupMembersError(data){
                AlertNotification.error("Error al intentar cargar los miembros del grupo. Vuelva a intentarlo mas tarde");
            }
        };

        vm.safeHtml = function(html){
            return $sce.trustAsHtml(html);
        };

        vm.remove_member = function(membership) {
            Group.remove_member(membership.id).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("Se ha eliminado un miembro del grupo con exito!!");
                //vm.group.splice(vm.items.indexOf(item),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar eliminar a un miembro del grupo");
            }
        };

        vm.confirm_request = function(membership){
            Group.memberships_requests_confirm(membership).then(requestConfirmSuccess, requestConfirmError);

            function requestConfirmSuccess(data){
                vm.memberships_requests.splice(vm.memberships_requests.indexOf(membership),1);
                var status_show = 'aceptado';
                if(membership.status == 3){
                    status_show = 'rechazado'
                }
                AlertNotification.error("Has " + status_show + " con exito!" );
            }

            function requestConfirmError(data){
                AlertNotification.error("Error al intentar confirmar la solicitud, vuelva a intentarlo mas tarde");
            }
        };

    }
})();