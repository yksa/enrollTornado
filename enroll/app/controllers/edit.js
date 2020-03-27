import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class EditController extends Controller {
    @action
    updateInfo(student){
        // name = return value from server
        student.save().then((name) => this.transitionToRoute('list')); 
    }
}
