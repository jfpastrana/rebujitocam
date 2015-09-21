# hackaffeine.com - Santi

SCRIPTS_FOLDER = "/home/pi/Proyectos/rebujitocam/scripts/"
TOSEND_FOLDER = "/home/pi/Proyectos/rebujitocam/toSend/"
USER_ALLOWED = "NAME"
function on_msg_receive (msg)
  if msg.out then
    return
  end
  
  -- Allowed only our ID's
  if (msg.from.print_name == USER_ALLOWED) then

   if (msg.text=='Foto') then
      os.execute('sh ' .. SCRIPTS_FOLDER .. 'startTweetting.sh')
   end	
  end 
     
end

function on_our_id (id)
end
   
function on_secret_chat_created (peer)
end
   
function on_user_update (user)
end
 
function on_chat_update (user)
end
 
function on_get_difference_end ()
end
 
function on_binlog_replay_end ()
end

function ok_cb(extra, success, result)
end
