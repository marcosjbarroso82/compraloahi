/**
 * ItemCtrl
 * @namespace dashBoardApp.item.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.item.controllers')
        .controller('ItemCtrl', ItemCtrl);

    ItemCtrl.$inject = ['$scope', 'Item', 'AlertNotification', 'ngTableParams', '$filter'];

    /**
     * @namespace ItemCtrl
     */
    function ItemCtrl($scope, Item, AlertNotification, ngTableParams, $filter) {

        var vm = this;

        // Declare functions
        vm.destroy = destroy;

        // Declare vars
        vm.items = [];

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
            total: vm.items.length, // length of data
            getData: function($defer, params) {
                // use build-in angular filter
                var filteredData = params.filter() ?
                    $filter('filter')(vm.items, params.filter()) :
                    vm.items;
                // use build-in angular filter
                var orderedData = params.sorting() ?
                    $filter('orderBy')(filteredData, params.orderBy()) :
                    filteredData;

                params.total(orderedData.length); // set total for recalc pagination
                $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });


        $scope.$watchCollection("vm.items", function () {
            vm.tableParams.reload();
        });

        function loadItems(page_nro){
            vm.promiseRequest = Item.list().then(getSuccess, getError);

            function getSuccess(data){
                vm.items = data.data.results;
                vm.request = true;
            }

            function getError(error){
                AlertNotification.error("Error al consultar avisos, vuelva a intentarlo mas tarde");

                vm.request = true;
            }

        }

        init();

        function init(){
            loadItems();
        }

        function destroy(item) {
            Item.destroy(item.id).then(deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                AlertNotification.success("El aviso " + item.title + " fue eliminado con exito!");
                vm.items.splice(vm.items.indexOf(item),1);
            }

            function deleteError(data, headers, status){
                AlertNotification.error("Error al intentar borrar el aviso");
            }
        }

    }
})();
