/**
 * GroupCtrl
 * @namespace dashBoardApp.group.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.group.controllers')
        .controller('GroupCtrl', GroupCtrl);

    GroupCtrl.$inject = ['$scope', 'Group', 'AlertNotification', 'ngTableParams', '$filter'];

    /**
     * @namespace GroupCtrl
     */
    function GroupCtrl($scope, Group, AlertNotification, ngTableParams, $filter) {

        var vm = this;

        // Declare functions
        vm.destroy = destroy;

        // Declare vars
        vm.groups = [];

        vm.request = false;

        vm.filters = {
            title: ''
        };

        vm.tableParams = new ngTableParams({
            page: 1,            // show first page
            count: 10,          // count per page
            filter: vm.filters,
            sorting: {
                title: 'asc'
            }
        }, {
            total: vm.groups.length, // length of data
            getData: function($defer, params) {
                // use build-in angular filter
                var filteredData = params.filter() ?
                    $filter('filter')(vm.groups, params.filter()) :
                    vm.groups;
                // use build-in angular filter
                var orderedData = params.sorting() ?
                    $filter('orderBy')(filteredData, params.orderBy()) :
                    filteredData;

                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });

        $scope.$watchCollection("vm.groups", function () {
            vm.tableParams.reload();
        });

        function loadGroups(page_nro){
            vm.promiseRequest = Group.list().then(getSuccess, getError);

            function getSuccess(data){
                console.log("GET DATA");
                console.log(data);
                vm.groups = data.data.results;
                vm.request = true;
            }

            function getError(error){
                AlertNotification.error("Error al consultar los grupos, vuelva a intentarlo mas tarde");

                vm.request = true;
            }

        }

        init();

        function init(){
            loadGroups();
        }

        function destroy(group) {
            Group.destroy(group.id).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("El grupo " + group.title + " fue eliminado con exito!");
                vm.groups.splice(vm.groups.indexOf(group),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar borrar el aviso");
            }
        }
    }
})();
