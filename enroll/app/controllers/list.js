import Controller from '@ember/controller';
import { action } from '@ember/object';


export default class ListController extends Controller {

   @action
   delete(params){
       let deleteStudent = this.store.peekRecord('student', params.id);
       deleteStudent.deleteRecord();
       deleteStudent.save();
   }
}


