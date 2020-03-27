import Model, { attr } from '@ember-data/model';

export default class StudentModel extends Model {
    @attr('string') name;
    @attr('string') bDate;
    @attr('string') address;
    @attr('string') phone;
}
