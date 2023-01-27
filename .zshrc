#
#     ██╗      █████╗ ██╗  ██╗███████╗██╗  ██╗███╗   ███╗██╗██╗  ██╗ █████╗ ███╗   ██╗████████╗ █████╗
#     ██║     ██╔══██╗██║ ██╔╝██╔════╝██║  ██║████╗ ████║██║██║ ██╔╝██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗
#     ██║     ███████║█████╔╝ ███████╗███████║██╔████╔██║██║█████╔╝ ███████║██╔██╗ ██║   ██║   ███████║
#     ██║     ██╔══██║██╔═██╗ ╚════██║██╔══██║██║╚██╔╝██║██║██╔═██╗ ██╔══██║██║╚██╗██║   ██║   ██╔══██║
#     ███████╗██║  ██║██║  ██╗███████║██║  ██║██║ ╚═╝ ██║██║██║  ██╗██║  ██║██║ ╚████║   ██║   ██║  ██║
#     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
#

#Locale for terminal
export LANG="en_IN.UTF-8"
export LC_ALL="en_IN.UTF-8"
export LC_CTYPE="en_IN.UTF-8"

###EXPORT
export TERM="xterm-256color"
export EDITOR="nvim" 
export VISUAL="nvim"

export SUDO_EDITOR="nvim"
alias "sudoedit"='function _sudoedit(){sudo -e "$1";};_sudoedit'

### NVM 
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

##### pnpm
export PNPM_HOME="/home/lakshmi/.local/share/pnpm"
export PATH="$PNPM_HOME:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$PATH:$HOME/.local/bin/"

### CHANGE TITLE OF TERMINALS
case ${TERM} in
  xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|alacritty|st|konsole*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
        ;;
  screen*)
    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
    ;;
esac
############################
####  Source plugins

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=242'
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
source ~/.zsh/git-flow-completion-master/git-flow-completion.zsh

##############################################################################
# History Configuration
##############################################################################
HISTSIZE=5000               #How many lines of history to keep in memory
HISTFILE=~/.zsh_history     #Where to save history to disk
SAVEHIST=5000               #Number of history entries to save to disk
#HISTDUP=erase               #Erase duplicates in the history file
setopt    appendhistory     #Append history to the history file (no overwriting)
setopt    sharehistory      #Share history across terminals
setopt    incappendhistory  #Immediately append to the history file, not just when a term is killed

########################################################################
###############                 FUNCTION                 ###############
########################################################################

############# Function extract for common file formats ###
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

function extract {
 if [ -z "$1" ]; then
    # display usage if no parameters given
    echo "Usage: extract <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz>"
    echo "       extract <path/file_name_1.ext> [path/file_name_2.ext] [path/file_name_3.ext]"
 else
    for n in "$@"
    do
      if [ -f "$n" ] ; then
          case "${n%,}" in
            *.cbt|*.tar.bz2|*.tar.gz|*.tar.xz|*.tbz2|*.tgz|*.txz|*.tar)
                         tar xvf "$n"       ;;
            *.lzma)      unlzma ./"$n"      ;;
            *.bz2)       bunzip2 ./"$n"     ;;
            *.cbr|*.rar)       unrar x -ad ./"$n" ;;
            *.gz)        gunzip ./"$n"      ;;
            *.cbz|*.epub|*.zip)       unzip ./"$n"       ;;
            *.z)         uncompress ./"$n"  ;;
            *.7z|*.arj|*.cab|*.cb7|*.chm|*.deb|*.dmg|*.iso|*.lzh|*.msi|*.pkg|*.rpm|*.udf|*.wim|*.xar)
                         7z x ./"$n"        ;;
            *.xz)        unxz ./"$n"        ;;
            *.exe)       cabextract ./"$n"  ;;
            *.cpio)      cpio -id < ./"$n"  ;;
            *.cba|*.ace)      unace x ./"$n"      ;;
            *)
                         echo "extract: '$n' - unknown archive method"
                         return 1
                         ;;
          esac
      else
          echo "'$n' - file does not exist"
          return 1
      fi
    done
fi
}

IFS=$SAVEIFS

############# navigation
up () {
  local d=""
  local limit="$1"

  # Default to limit of 1
  if [ -z "$limit" ] || [ "$limit" -le 0 ]; then
    limit=1
  fi

  for ((i=1;i<=limit;i++)); do
    d="../$d"
  done

  # perform cd. Show error if cd fails
  if ! cd "$d"; then
    echo "Couldn't go up $limit dirs.";
  fi
}


########################################################################
###########                 ZSH KeyBinding            ##################
########################################################################
# create a zkbd compatible hash;
# to add other keys to this hash, see: man 5 terminfo
typeset -g -A key

key[Home]="${terminfo[khome]}"
key[End]="${terminfo[kend]}"
key[Insert]="${terminfo[kich1]}"
key[Backspace]="${terminfo[kbs]}"
key[Delete]="${terminfo[kdch1]}"
key[Up]="${terminfo[kcuu1]}"
key[Down]="${terminfo[kcud1]}"
key[Left]="${terminfo[kcub1]}"
key[Right]="${terminfo[kcuf1]}"
key[PageUp]="${terminfo[kpp]}"
key[PageDown]="${terminfo[knp]}"
key[Shift-Tab]="${terminfo[kcbt]}"

# setup key accordingly
[[ -n "${key[Home]}"      ]] && bindkey -- "${key[Home]}"       beginning-of-line
[[ -n "${key[End]}"       ]] && bindkey -- "${key[End]}"        end-of-line
[[ -n "${key[Insert]}"    ]] && bindkey -- "${key[Insert]}"     overwrite-mode
[[ -n "${key[Backspace]}" ]] && bindkey -- "${key[Backspace]}"  backward-delete-char
[[ -n "${key[Delete]}"    ]] && bindkey -- "${key[Delete]}"     delete-char
[[ -n "${key[Up]}"        ]] && bindkey -- "${key[Up]}"         up-line-or-history
[[ -n "${key[Down]}"      ]] && bindkey -- "${key[Down]}"       down-line-or-history
[[ -n "${key[Left]}"      ]] && bindkey -- "${key[Left]}"       backward-char
[[ -n "${key[Right]}"     ]] && bindkey -- "${key[Right]}"      forward-char
[[ -n "${key[PageUp]}"    ]] && bindkey -- "${key[PageUp]}"     beginning-of-buffer-or-history
[[ -n "${key[PageDown]}"  ]] && bindkey -- "${key[PageDown]}"   end-of-buffer-or-history
[[ -n "${key[Shift-Tab]}" ]] && bindkey -- "${key[Shift-Tab]}"  reverse-menu-complete

# Finally, make sure the terminal is in application mode, when zle is
# active. Only then are the values from $terminfo valid.
if (( ${+terminfo[smkx]} && ${+terminfo[rmkx]} )); then
	autoload -Uz add-zle-hook-widget
	function zle_application_mode_start { echoti smkx }
	function zle_application_mode_stop { echoti rmkx }
	add-zle-hook-widget -Uz zle-line-init zle_application_mode_start
	add-zle-hook-widget -Uz zle-line-finish zle_application_mode_stop
fi


########################################################################
###############               ALIASES                 ##################
########################################################################

#### XAMPP 
alias xampp='sudo /opt/lampp/lampp'

#Node.Js
alias snpm="sudo npm"
alias pn='pnpm'
alias spn='sudo pnpm'

#vim
alias vim="$EDITOR"
alias svim="sudo $EDITOR"

#Make a directory with parent-child
alias mkdir="mkdir -p"

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'
alias rmf='rm -rf'

#Custom Clear command
alias clr='clear;colorscript random'

#java runtime
alias jar='java -jar'

# fastboot sudo permition
alias fastboot='sudo fastboot'

#dd command
alias dd='sudo dd bs=4M status=progress'

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# Changing "ls" to "exa"
alias ls='exa -alh --color=always --group-directories-first' # listing
alias la='exa -ah --color=always --group-directories-first'  # all files and dirs
alias ll='exa -lh --color=always --group-directories-first'  # long format
alias lt='exa -aTh --color=always --group-directories-first' # tree listing
alias l.='exa -ah | egrep "^\."'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

#dnf command
alias pacins='sudo dnf install'
alias pacrmv='sudo dnf remove --noautoremove'
alias pacrmvwd='sudo dnf remove'
alias pacup='sudo dnf update systemd'
alias search='dnf search'
alias cleanup='sudo dnf autoremove'
alias dnflist='dnf grouplist'
alias groupins='sudo dnf groupinstall'
alias grouprmv='sudo dnf groupremove'

#Source config
alias fsource='source ~/.config/fish/config.fish'
alias bsource='source ~/.bashrc'
alias zsource='source ~/.zshrc'

#wifi & bluetooth
alias wifi="nmtui"
alias blue="blueberry"

#font listing
alias flist='fc-list | grep'

#chmod
alias mod="sudo chmod +x"

#change ownership
alias ownfi='sudo chown $USER'
alias ownfo='sudo chown -R $USER'

# git
alias gst='git status'
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias tag='git tag'
alias newtag='git tag -a'
alias gemail='git config --global user.email'
alias gname='git config --global user.name'

#list all drive with UUID
alias list_drive='lsblk -f'

#continue download
alias wget="wget -c"

#userlist
alias userlist="cut -d: -f1 /etc/passwd"

#grub update
alias grub-update="sudo grub2-mkconfig -o /boot/grub2/grub.cfg"

#get the error messages from journalctl
alias jctl="journalctl -p 3 -xb"

#Edit with your EDITOR for important configuration files
alias nlightdm="sudo $EDITOR /etc/lightdm/lightdm.conf"
alias ngrub="sudo $EDITOR /etc/default/grub"
alias nconfgrub="sudo $EDITOR /boot/grub/grub.cfg"
alias nmkinitcpio="sudo $EDITOR /etc/mkinitcpio.conf"
alias nsddm="sudo $EDITOR /usr/lib/sddm/sddm.conf.d/default.conf"
alias nfstab="sudo $EDITOR /etc/fstab"
alias nbash="$VISUAL ~/.bashrc"
alias nzsh="$VISUAL ~/.zshrc"
alias nfish="$VISUAL ~/.config/fish/config.fish"
alias nbspwm="$VISUAL ~/.config/bspwm/bspwmrc"
alias nsxhkd="$VISUAL ~/.config/sxhkd/sxhkdrc"
alias nsourcelist="sudo $EDITOR /etc/apt/sources.list"

#Edit config file for ricing
alias ni3="$VISUAL ~/.config/i3/config"
alias ni3blocks="$VISUAL ~/.config/i3/i3blocks.conf"
alias nqtile="$VISUAL ~/.config/qtile/config.py"
alias npolybar="$VISUAL ~/.config/polybar/config"
alias nkitty="$VISUAL ~/.config/kitty/kitty.conf"
alias nalacritty="$VISUAL ~/.config/alacritty/alacritty.yml"
alias npicom="$VISUAL ~/.config/picom/picom.conf"
alias nxresources="$VISUAL ~/.Xresources"
alias nstarship="$VISUAL ~/.config/starship.toml"
alias nneofetch="$VISUAL ~/.config/neofetch/config.conf"
alias nnvim='$VISUAL ~/.config/nvim/init.lua'
#systeminfo
alias probe="sudo -E hw-probe -all -upload"
alias sysfailed="systemctl list-units --failed"

#shutdown or reboot
alias shutdown="shutdown now"

#give the list of all installed desktops - xsessions desktops
alias xd="ls /usr/share/xsessions"

# switch between shells
# I do not recommend switching default SHELL from bash.
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Now log out.'"

########################################################################
###############                   Styling                ###############
########################################################################
neofetch --ascii ~/.config/neofetch/images/redhat.txt

#starship startup scripts
eval "$(starship init zsh)"
