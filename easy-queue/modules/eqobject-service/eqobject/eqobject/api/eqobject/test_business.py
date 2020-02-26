import unittest
from easyqueue.eqobject.api.eqobject.business import (
    create_eq_object, create_eq_objects, request_eq_object, request_eq_objects, update_eq_object, delete_eq_object)

class TestEQObject(unittest.TestCase):

    def setUp(self):
        self.examples_eqobject_json = [
            {
                "_id": "1c482525eaa14c3d808de7d1d1a483ed",
                "__type__": "EQObject",
                "_created_at": "2020-01-01T16:57:53.501633"
            }, 
            {
                "_id": "2c482525eaa14c3d808de7d1d1a483ed",
                "__type__": "EQObject",
                "_created_at": "2020-01-02T16:57:53.501633"
            }, 
            {
                "_id": "3c482525eaa14c3d808de7d1d1a483ed",
                "__type__": "EQObject",
                "_created_at": "2020-01-03T16:57:53.501633"
            }
        ]

    @unittest.skip("debuggin")
    def test_create_eq_object(self):
        res = create_eq_object(self.examples_eqobject_json[0])
        self.assertEqual(res, dict(acknowledged=True, inserted_id=self.examples_eqobject_json[0]["_id"]))

    @unittest.skip("debuggin")
    def test_create_eq_objects(self):
        res = create_eq_objects(self.examples_eqobject_json[1:])
        self.assertEqual(res, dict(acknowledged=True, inserted_ids=[f["_id"] for f in self.examples_eqobject_json[1:]]))

    @unittest.skip("debuggin")
    def test_request_eq_object(self):
        res = request_eq_object(self.examples_eqobject_json[0]["_id"])
        self.assertEqual(res.json(), self.examples_eqobject_json[0])
    
    @unittest.skip("debuggin")
    def test_update_eq_object(self):
        data = dict(self.examples_eqobject_json[2])
        data["_created_at"] = "2000-01-01T16:57:53.501633"
        res = update_eq_object(self.examples_eqobject_json[2]["_id"], data)
        self.assertTrue(res["acknowledged"])

    @unittest.skip("debuggin")
    def test_delete_eq_object(self):
        res = delete_eq_object(self.examples_eqobject_json[0]["_id"])
        self.assertTrue(res["acknowledged"])
  
    @unittest.skip("debuggin")
    def test_request_eq_objects(self):
        res0 = request_eq_objects()
        res1 = request_eq_objects(skip=1)
        res2 = request_eq_objects(limit=1)
        res3 = request_eq_objects(skip=1, limit=1)
        self.assertEqual(3, len(res0))
        self.assertEqual(2, len(res1))
        self.assertEqual(1, len(res2))
        self.assertEqual(1, len(res3))
  


if __name__ == '__main__':
    unittest.main()