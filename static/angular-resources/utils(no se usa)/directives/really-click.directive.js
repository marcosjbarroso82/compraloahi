/**
 * 
 * @namespace App.util.directives
 */
 (function () {
  'use strict';

  angular
  .module('App.util.directives')
  .directive('ngReallyClick', ngReallyClick);

  ngReallyClick.$inject = ['$modal'];

    /**
     * @namespace Dynamic field
     */
     function ngReallyClick($modal) {
        /**
         * @name ngReallyClick
         * @desc The directive to be returned
         * @memberOf App.util.directives.countries
         */
         var ModalInstanceCtrl = function($scope, $modalInstance) {
          $scope.ok = function() {
            $modalInstance.close();
          };

          $scope.cancel = function() {
            $modalInstance.dismiss('cancel');
          };
        };

        return {
          restrict: 'A',
          scope:{
    ngReallyClick:"&", //declare a function binding for directive
    item:"=" //the current item for the directive
  },
  link: function(scope, element, attrs) {
    element.bind('click', function() {
      var message = attrs.ngReallyMessage || "Are you sure ?";

            /*
            //This works
            if (message && confirm(message)) {
              scope.$apply(attrs.ngReallyClick);
            }
            //*/

            //*This doesn't work
            var modalHtml = '<div class="modal-body">' + message + '</div>';
            modalHtml += '<div class="modal-footer"><button class="btn btn-primary" ng-click="ok()">OK</button><button class="btn btn-warning" ng-click="cancel()">Cancel</button></div>';

            var modalInstance = $modal.open({
              template: modalHtml,
              controller: ModalInstanceCtrl
            });

            modalInstance.result.then(function() {
              scope.ngReallyClick({item:scope.item}); //call the function though function binding
            }, function() {
              //Modal dismissed
            });
            //*/

          });

  }
};

}
})();