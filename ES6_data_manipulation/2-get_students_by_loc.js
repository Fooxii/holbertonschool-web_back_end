export default function getStudentsByLocation(objList, city) {
  return objList.filter(student => student.location === city);
}
