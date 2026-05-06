export default function getListStudentIds(objList) {
  if (Array.isArray(objList) !== true) {
    return [];
  }
  const idList = objList.map(student => student.id);
  return idList;
}
