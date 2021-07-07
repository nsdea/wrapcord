import wrapcord

print('################### ', 1)
test_channel = wrapcord.Channel(840878311008763914)
print('################### ', 2)
message = test_channel.send('Hello!')
print('################### ', 3)
message.react('🔥')
print('################### ', 4)