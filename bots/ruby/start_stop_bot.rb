require "telegram/bot"

token = File.open("../../ttoken", "r") {|f| f.readline}

Telegram::Bot::Client.run(token) do |bot|
	bot.listen do |message|
		case message.text
		when '/start'
			bot.api.send_message(chat_id: message.chat.id, text: "Hello, #{message.from.first_name}")
		when '/stop'
			bot.api.send_message(chat_id: message.chat.id, text: "Bye, #{message.from.first_name}")
		end
	end
end
