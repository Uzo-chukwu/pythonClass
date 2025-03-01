import unittest
from tv.src.tv_app.tv import Television

class MyTestCase(unittest.TestCase):
    def setUp(self):
         self.tv = Television()



    def test_default_state_of_tv_is_off(self):
        actual = self.tv.is_on
        expected = False
        self.assertEqual(actual, expected)

    def test_default_channel_is_1(self):
        actual = self.tv.channel
        expected = 1
        self.assertEqual(actual, expected)

    def test_default_volume_is_0(self):
        actual = self.tv.volume_level
        expected = 0
        self.assertEqual(actual, expected)

    def test_tv_can_be_turned_on(self):
        self.tv.turn_on()
        actual = self.tv.is_on
        expected = True
        self.assertEqual(actual, expected)

    def test_tv_can_be_turned_off(self):
        self.tv.turn_off()
        actual = self.tv.is_on
        expected = False
        self.assertEqual(actual, expected)

    def test_that_volume_Can_be_increased_by_1(self):
        self.assertEqual(self.tv.volume_level, 0)
        self.tv.turn_on()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level, 1)

    def test_that_volume_Can_be_decreased_by_1(self):
        self.tv.turn_on()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level, 3)
        self.tv.volume_down()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_level, 1)

    def test_that_volume_only_be_changed_when_tv_is_on(self):
        self.assertEqual(self.tv.volume_level, 0)
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level, 0)
        self.tv.turn_on()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level, 3)
        self.tv.volume_down()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_level, 1)

    def test_that_channel_number_can_be_increased_by_one(self):
        self.tv.turn_on()
        self.tv.channel = 1
        self.assertEqual(self.tv.channel,1)
        self.tv.channel_up()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, 3)

    def test_that_channel_number_can_be_decreased_by_one(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.channel, 1)
        for i in range (8): self.tv.channel_up()
        for i in range (6):self.tv.channel_down()


        self.assertEqual(self.tv.channel, 3)

    def test_that_channel_number_can_be_changed_only_when_tv_is_on(self):

        self.assertEqual(self.tv.channel, 1)
        for count in range (8): self.tv.channel_up()
        for count in range (6):self.tv.channel_down()
        self.assertEqual(self.tv.channel, 1)
        self.tv.turn_on()
        for count in range (8): self.tv.channel_up()
        for count in range (6):self.tv.channel_down()
        self.assertEqual(self.tv.channel, 3)

    def test_that_channel_be_set_by_inputing_number(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.channel,1)
        self.tv.set_channel(23)
        self.assertEqual(self.tv.channel,23)

    def test_that_volume_can_muted(self):
        self.tv.turn_on()
        self.tv.mute()
        self.assertTrue(self.tv.is_mute)

    def test_that_volume_can_be_unmuted(self):
        self.tv.turn_on()
        self.tv.mute()
        self.assertTrue(self.tv.is_mute)
        self.tv.unmute()
        self.assertFalse(self.tv.is_mute)























if __name__ == '__main__':
    unittest.main()
