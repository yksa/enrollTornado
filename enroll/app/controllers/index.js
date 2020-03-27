import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class FormController extends Controller {
    @action
    saveInfo(){
        let data = { name: this.get('name'), bDate: this.get('bDate'), address: this.get('address'), phone: this.get('phone') };
        console.log(data);
        let newStudent = this.store.createRecord('student', data);
        console.log(newStudent);
        newStudent.save();
        this.set('name','');
        this.set('bDate','');
        this.set('address','');
        this.set('phone','');
    }
}
