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
            Post.list().then(successGetPosts, errorGetPosts);

            function successGetPosts(data){
                vm.posts = data.data.results;
            }

            function errorGetPosts(data){
                AlertNotification.error("Error al intentar cargar los post, vuelva a intentarlo mas tarde.");
            }
        }

        vm.inviteMember = function(){
            Group.invite(group, { 'email':vm.member_email }).then(InviteMemberSuccess, InviteMemberError);

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
            if (!flag_get_user){
                flag_get_user = true;
                Group.members(group).then(getGroupMembersSuccess, getGroupMembersError)
            }

            function getGroupMembersSuccess(data){
                vm.group = data.data
            }

            function getGroupMembersError(data){
                AlertNotification.error("Error al intentar cargar los miembros del grupo. Vuelva a intentarlo mas tarde");
            }
        };

        vm.safeHtml = function(html){
            return $sce.trustAsHtml(html);
        };

        vm.remove_member = function(member) {
            Group.remove_member(group, member).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("Se ha eliminado un miembro del grupo con exito!!");
                //vm.group.splice(vm.items.indexOf(item),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar eliminar a un miembro del grupo");
            }
        };

    }
})();